from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import PostagemLivros, Cadastro
from .forms import ContaForm

class HomePage(ListView):
    model = PostagemLivros
    template_name = 'paginas/home.html'

class Cadastro(CreateView):
    model = Cadastro
    form_class = ContaForm
    template_name = 'paginas/criar_conta.html'