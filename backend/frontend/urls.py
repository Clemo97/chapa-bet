from django.urls import path
from . import views

urlpatterns = [
	path('', views.list, name="list"),
    path('index.html', views.list, name="list"),
	path('signup.html', views.signup, name="signup"),
	path('login.html', views.login, name="login"),
    path('cart.html', views.cart_view, name='cart'),
]
