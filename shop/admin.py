from django.contrib import admin
from .models import Product, Category, Image

# Register your models here.
admin.site.register(Category)


class ImageInline(admin.TabularInline):
    model = Image


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


admin.site.register(Product, ProductAdmin)
