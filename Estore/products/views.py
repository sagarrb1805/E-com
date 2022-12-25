from django.shortcuts import render
from .models import Category, Product, ProductImages

def home_view(request):
    categories = Category.objects.all()

    return render(request, 'products/home.html', {'categories':categories})