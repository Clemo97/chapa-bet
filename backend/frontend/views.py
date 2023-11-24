from django.shortcuts import render

# Create your views here.

def list(request):
	return render(request, 'frontend/index.html')

def signup(request):
	return render(request, 'frontend/signup.html')

def login(request):
	return render(request, 'frontend/login.html')
