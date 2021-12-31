from django.contrib import admin
from .models import Product, Category, Image, Cart

# Register your models here.
admin.site.register(Category)


class ImageInline(admin.TabularInline):
    model = Image


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Cart)

