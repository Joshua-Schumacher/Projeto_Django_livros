from django.shortcuts import render
from django.views.generic import ListView
from .models import PostagemLivros

class HomePage(ListView):
    model = PostagemLivros
    template_name = 'paginas/home.html'