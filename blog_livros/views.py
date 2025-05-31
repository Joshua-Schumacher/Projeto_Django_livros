from django.shortcuts import render
from django.views.generic import ListView
from .models import Livros

class HomePage(ListView):
    model = Livros
    template_name = 'paginas/home.html'