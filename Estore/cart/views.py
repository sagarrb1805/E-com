from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from products.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


@login_required
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart_item = Cart.objects.get(user=request.user, product=product)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except Cart.DoesNotExist:
        cart_item = Cart.objects.create(user=request.user, product=product, quantity=1)
        cart_item.save()

    return redirect('cart:cart_detail')


@login_required
def cart_remove(request, product_id):

    
    # product = get_object_or_404(Product, id=product_id)
    product = Product.objects.get(id=product_id)
    cart_item = Cart.objects.get(user=request.user, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')



@login_required
def full_remove(request, product_id):
   
    # product = get_object_or_404(Product, id=product_id)
    product = Product.objects.get(id=product_id)
    cart_item = Cart.objects.get(user=request.user, product=product)
    cart_item.delete()
    return redirect('cart:cart_detail')
    
@login_required
def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart_items = Cart.objects.filter(user=request.user)
        for cart_item in cart_items:
            total += cart_item.product.product_price * cart_item.quantity
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart/cart.html', {'cart_items':cart_items, 'total':total, 'counter':counter})


