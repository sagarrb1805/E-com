from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def sub_total(self):
        return self.product.product_price * self.quantity

    def __str__(self):
        return "{}".format(self.product)
