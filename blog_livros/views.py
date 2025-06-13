from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView, DeleteView, View
from .models import Cadastro, PostagemLivros 
from .forms import ContaForm, PostagemForm
from django.urls import reverse_lazy

class HomePage(ListView):
     def get(self,request):
        return render(request,'paginas/home.html')

""" 
    model = PostagemLivros
    template_name = 'paginas/home.html' """

class Cadastro(CreateView):
    model = Cadastro
    form_class = ContaForm
    template_name = 'paginas/criar_conta.html'
    success_url = reverse_lazy('home')


class PostagemLivros(CreateView):
    model = PostagemLivros
    form_class = PostagemForm
    template_name = 'paginas/criar_postagem.html'

class Biblioteca(ListView):
    model = PostagemLivros
    template_name  = 'paginas/biblioteca.html'


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

class Editar(UpdateView):
    model = PostagemLivros
    form_class = PostagemForm
    template_name = 'paginas/criar_postagem.html'   
    
    #Deixa dinamico dados no html
    def get_context_data(self, **kwargs):
        #**kwargs - espera qualquer argumento
        context = super().get_context_data(**kwargs) #Cria o context
        context['titulo'] = 'Edição do Post'
        context['botao'] = 'Editar'
        return context
    success_url = reverse_lazy('biblioteca')

#Classe exlcuir

class Deletar(DeleteView):
    model = PostagemLivros
    template_name = 'paginas/'
    success_url = reverse_lazy('biblioteca')



class Login(View):
    
    def get(self, request):
        return render (request, 'paginas/login.html')
    # A partir daqui vamos:
    # Identificar o apelido e o senha do formulario, identificar o cliente e criar a sessão
   
    def post(self, request, *args, **kwargs):
        apelido = request.POST.get('apelido')
        senha = request.POST.get('senha')
 
        if apelido and senha:
            usuario = Cadastro # Puxa o primeiro cliente com o apelido e senha
            
            if usuario:
                #Vamos criar as seções
                request.session['apelido_usuario'] = usuario
                return render(request, 'paginas/login.html') 
            else:
                erro_message = "Nenhum cliente encontrado!"
                return render(request, 'paginas/login.html',{'mensagem':erro_message})
 
 
        else:
            erro_message = "Por Favor, informe um apelido e senha para consulta"
            return render(request, 'paginas/login.html',{'mensagem':erro_message})