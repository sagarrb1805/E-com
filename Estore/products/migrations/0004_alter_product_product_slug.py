# Generated by Django 4.1 on 2022-12-24 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_products_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
