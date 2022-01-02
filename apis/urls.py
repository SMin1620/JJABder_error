from django.urls import path
from .views import CartCreateView


urlpatterns = [
    # cart
    path('v1/cart/create/', CartCreateView.as_view(), name='apis_v1_cart_create'),
]