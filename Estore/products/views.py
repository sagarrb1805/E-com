from django.shortcuts import render
from .models import Category, Product, ProductImages

def home_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'products/home.html', {'categories':categories, 'products':products})