# Generated by Django 4.1 on 2022-12-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_product_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
