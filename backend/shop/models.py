from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    promotional_price = models.DecimalField(max_digits=10, decimal_places=2)
    savings_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    image_url = models.CharField(max_length=200, default="https://images.pexels.com/photos/90946/pexels-photo-90946.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    weight_or_volume = models.CharField(max_length=20)  # Kilogram/Litre or Size (S/L/XL)

    # Other fields as per your requirements

    def __str__(self):
        return self.name
    
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='pending')  # Define choices for status
    payment_method = models.CharField(max_length=50, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    # Other fields as needed

    # Methods for total order price calculation, status updates, etc.

    def __str__(self):
        product_quantities = ', '.join([f'{item.product} (Qty: {item.quantity})' for item in self.orderitem_set.all()])
        return f"Order ID: {self.pk} | User: {self.user.username} | Products: {product_quantities}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # Other fields related to order item

    def subtotal(self):
        return self.quantity * self.product.promotional_price

    # Other methods as per your requirements

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.pk}"
