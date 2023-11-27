from rest_framework import serializers
from .models import Product, Order, OrderItem
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"  # Add more fields as needed

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'subtotal')  # Add more fields as needed

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='orderitem_set', many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'created_at', 'updated_at', 'status', 'payment_method', 'transaction_id', 'user', 'items', 'total_price')

    def get_total_price(self, obj):
        total = sum(item.subtotal() for item in obj.orderitem_set.all())
        return total


class UserOrdersListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve orders belonging to the logged-in user
        user = self.request.user
        orders = Order.objects.filter(user=user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
