from django.urls import path
from .views import ProductDetailView, OrderCreate, ProductListView, UserOrdersListView, OrderItemDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),  # For listing all products and creating a new one
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  # For accessing individual products
    path('orders/create/', OrderCreate.as_view(), name='order-create'),
    path('orders/user/', UserOrdersListView.as_view(), name='user-orders'),
    path('orderitems/<int:pk>/', OrderItemDetailView.as_view(), name='orderitem-detail'),  # Add the new view for OrderItem
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)