from django.urls import path
from .views import CartCreateView
from .views import UserLoginView, UserLogoutView, UserCreateView


urlpatterns = [
    # User
    path('v1/user/login/', UserLoginView.as_view(), name='apis_v1_user_login'),
    path('v1/user/logout/', UserLogoutView.as_view(), name='apis_v1_user_logout'),
    path('v1/user/register/', UserCreateView.as_view(), name='apis_v1_user_register'),

    # Cart
    path('v1/cart/create/', CartCreateView.as_view(), name='apis_v1_cart_create'),
]