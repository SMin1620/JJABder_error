from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Product, Category



# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['products'] = Product.objects.all()

        return context



class IntroView(TemplateView):
    template_name = 'intro.html'



