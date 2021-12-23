from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'


class LoginView(TemplateView):
    template_name = 'my_account/login.html'


class RegisterView(TemplateView):
    template_name = 'my_account/join_us.html'

