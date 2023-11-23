# shop/admin.py

from django.contrib import admin
from .models import Product, Order, OrderItem

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'get_products')  # Display fields in the admin list view

#     def get_products(self, obj):
#         return ", ".join([str(product) for product in obj.products.all()])  # Display associated products

# admin.site.register(Order, OrderAdmin)



