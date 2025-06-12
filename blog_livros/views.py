from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView
from .models import PostagemLivros, Cadastro
from .forms import ContaForm, PostagemForm
from django.urls import reverse_lazy

class HomePage(ListView):
    model = PostagemLivros
    template_name = 'paginas/home.html'

class Cadastro(CreateView):
    model = Cadastro
    form_class = ContaForm
    template_name = 'paginas/criar_conta.html'

    success_url = reverse_lazy('paginas/home.html')

   

class PostagemLivros(CreateView):
    model = PostagemLivros
    form_class = PostagemForm
    template_name = 'paginas/criar_postagem.html'


class PostagemUpdate(UpdateView):
    model = PostagemLivros    
    template_name = 'paginas/criar_postagem.html'    
    form_class = PostagemForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Resenha'
        context['botao'] = 'Salvar'
        return context
    
    success_url = reverse_lazy('list_cliente')

