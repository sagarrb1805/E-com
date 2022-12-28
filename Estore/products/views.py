from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage 


from .models import Category, Product, ProductImages


def home_view(request, category=None):
    categories = Category.objects.all()
    products = None
    if category is None:
        products = Product.objects.all()
    else:
        category_name = get_object_or_404(Category, category_slug=category)
        products = Product.objects.all().filter(product_category=category_name)

    paginator = Paginator(products, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'products/home.html', {'categories':categories, 'products':products})