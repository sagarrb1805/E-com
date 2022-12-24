from django.contrib import admin
from .models import Category, Product, ProductImages

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_image']

class ProductImagesInline(admin.StackedInline):
    model = ProductImages
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]
    list_display = ['product_name', 'product_category', 'product_price']
    readonly_fields = ['product_slug', 'product_final_price']


admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages)
