from django.utils.text import slugify
import random

def slugify_category_name(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.category_name)
    Klass = instance.__class__
    qs = Klass.objects.filter(category_slug=slug).exclude(id=instance.id)

    if qs.exists():
        rand_int = random.randint(100000, 900000)
        slug = f"{slug}-{rand_int}"
        return slugify_name(instance, new_slug=slug)
    instance.category_slug = slug
    return instance



def slugify_name(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.product_name)
    Klass = instance.__class__
    qs = Klass.objects.filter(product_slug=slug).exclude(id=instance.id)

    if qs.exists():
        rand_int = random.randint(100000, 900000)
        slug = f"{slug}-{rand_int}"
        return slugify_name(instance, new_slug=slug)
    instance.product_slug = slug
    return instance

def calculate_final_price(instance):
    
    instance.product_final_price = instance.product_price - ((instance.product_price*instance.product_discount)/100)
    return instance