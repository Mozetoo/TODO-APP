from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView


# Create your views here.

class Login(TemplateView):
    template_name = 'cred/login.html'


class SignUp(TemplateView):
    template_name = 'cred/signup.html'
