from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView


# Create your views here.


class Home(TemplateView):
    template_name = 'home/index.html'
