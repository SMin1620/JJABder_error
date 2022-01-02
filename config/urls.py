"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.shortcuts import redirect

from shop.views import HomeView, ProductListView, category_page, ProductDetailView, CartView


class NonUserTemplateView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect('home')
        return super(NonUserTemplateView, self).dispatch(request, *args, **kwargs)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('apis/', include('apis.urls')),

    # product
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<str:slug>/', category_page, name='product_category'),
    path('cart/', CartView.as_view(), name='cart'),

    # user
    path('login/', NonUserTemplateView.as_view(template_name='login.html'), name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
