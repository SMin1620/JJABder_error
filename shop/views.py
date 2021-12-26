from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Product, Category


# Create your views here.
# 홈
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['products'] = Product.objects.all()

        return context


# 인트로
class IntroView(TemplateView):
    template_name = 'intro.html'


# 상품 전체 리스트
class ProductListView(TemplateView):
    model = Product
    template_name = 'store/product_list.html'
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)

        context['products'] = Product.objects.all()

        return context


# 네비게이션 용 카테고리 리스트


# 카테고리 별 리스트
def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'product_list': Product.objects.filter(category=category)
    }

    return render(request, 'store/product_list.html', context)

