from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from .utils import slugify_name, slugify_category_name, calculate_final_price

def product_pre_save(sender, instance, *args, **kwargs):
    if instance.product_slug == None:
        slugify_name(instance)
    if instance.product_final_price == None:
        calculate_final_price(instance)
def category_pre_save(instance, *args, **kwargs):
    slugify_category_name(instance)

class Category(models.Model):
    category_name = models.CharField(max_length=250)
    category_slug = models.SlugField(unique=True, max_length=250, null=True, blank=True)
    category_image = models.ImageField(upload_to='CategoryImages/')

    def get_category_url(self):
        return reverse("products:home_view",kwargs={'category':self.category_slug})

    def __str__(self):
        return self.category_name

pre_save.connect(category_pre_save, sender=Category)



class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_description = models.TextField(null=True, blank=True)
    product_price = models.IntegerField()
    product_discount = models.IntegerField(null=True, blank=True, default=0)
    product_final_price = models.IntegerField()
    product_slug = models.SlugField(unique=True, max_length=250, null=True, blank=True)
    product_category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)
    product_img = models.ImageField(upload_to='ProductImages', null=True, blank=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("products:product_detail_view", kwargs={'cat':self.product_category.category_slug, 'prd':self.product_slug})


pre_save.connect(product_pre_save, sender=Product)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='ProductImages')

    def __str__(self):
        return self.product.product_name
