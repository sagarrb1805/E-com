from django.db import models
from django.db.models.signals import pre_save
from .utils import slugify_product_title, calculate_final_price

def product_pre_save(sender, instance, *args, **kwargs):
    if instance.product_slug == None:
        slugify_product_title(instance)
    if instance.product_final_price == None:
        calculate_final_price(instance)


class Category(models.Model):
    category_name = models.CharField(max_length=250)
    category_image = models.ImageField(upload_to='CategoryImages/')

    def __str__(self):
        return self.category_name



class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_description = models.TextField(null=True, blank=True)
    product_price = models.FloatField()
    product_discount = models.FloatField(null=True, blank=True)
    product_final_price = models.FloatField()
    product_slug = models.SlugField(unique=True, max_length=250, null=True, blank=True)
    product_category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.product_name


pre_save.connect(product_pre_save, sender=Product)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='ProductImages')

    def __str__(self):
        return self.product.product_name
