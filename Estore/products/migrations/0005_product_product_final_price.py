# Generated by Django 4.1 on 2022-12-24 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_final_price',
            field=models.FloatField(default=23.5),
            preserve_default=False,
        ),
    ]
