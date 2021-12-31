from django.db import models


# Create your models here.

def image_upload_path(instance, filename):
    return 'product_{} / {}'.format(instance.product.id, filename)


# 카테고리 모델
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/product/{self.slug}/'


# 상품 모델
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    img_url = models.URLField('url', unique=True, null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', null=True, blank=True)

    def __str__(self):
        return '{} : {}'.format(self.title, self.price)

    def get_absolute_url(self):
        return f'/product/{self.pk}/'


# 이미지 모델
class Image(models.Model):
    UPLOAD_PATH = 'product-upload'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image_product')
    image = models.ImageField(upload_to='product/')


# 장바구니 모델
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    # total
    def sub_total(self):
        return self.product.price * self.quantity




