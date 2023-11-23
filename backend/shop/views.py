from rest_framework.generics import CreateAPIView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, Product, OrderItem
from .serializers import OrderItemSerializer, OrderSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny


@method_decorator(csrf_exempt, name='dispatch')
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class OrderCreate(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # Automatically set the user making the request as the user for this order
        serializer.save(user=self.request.user, status='pending')  # Set order status to 'pending'

    def create(self, request, *args, **kwargs):
        user = self.request.user
        pending_orders = Order.objects.filter(user=user, status='pending')

        if pending_orders.exists():
            # Return a message or redirect the user to the existing order
            return Response({'message': 'You already have a pending order.'}, status=status.HTTP_400_BAD_REQUEST)

        # Proceed with creating a new order if no pending orders exist
        return super().create(request, *args, **kwargs)


class UserOrdersListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve orders belonging to the logged-in user
        user = self.request.user
        orders = Order.objects.filter(user=user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    
class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)