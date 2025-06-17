from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView, DeleteView, View
from .models import Cadastro, PostagemLivros 
from .forms import ContaForm, PostagemForm
from django.urls import reverse_lazy

class HomePage(ListView):
     def get(self,request):
        return render(request,'paginas/home.html')



class Cadastro_page(CreateView):
    model = Cadastro
    form_class = ContaForm
    template_name = 'paginas/criar_conta.html'
    success_url = reverse_lazy('home')


class PostagemLivros_page(CreateView):
    model = PostagemLivros
    form_class = PostagemForm
    template_name = 'paginas/criar_postagem.html'
    success_url = reverse_lazy('biblioteca')
    

class Biblioteca(ListView):
    model = PostagemLivros
    context_object_name = 'postagem'
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
    
    success_url = reverse_lazy('biblioteca')


#Classe exlcuir

class Deletar(DeleteView):
    model = PostagemLivros
    template_name = 'paginas/deletar.html'
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
            usuario = Cadastro.objects.filter(apelido=apelido, senha=senha).first() # Puxa o primeiro cliente com o apelido e senha
            
            if usuario:
                #Vamos criar as seções
                request.session['apelido_usuario'] = usuario.apelido
                return render(request, 'paginas/home.html') 
            else:
                erro_message = "Nenhum cliente encontrado!"
                return render(request, 'paginas/login.html',{'mensagem':erro_message})
 
 
        else:
            erro_message = "Por Favor, informe um apelido e senha para consulta"
            return render(request, 'paginas/login.html',{'mensagem':erro_message})


class Logout(View):
    #Metodo que verifica e encerra a sessão
    def get(self, request): 
        if 'apelido_usuario' in request.session:
            del request.session['apelido_usuario']

        erro_message = 'Você foi desconectado!'
        return render(request, 'paginas/logout.html', {'mensagem': erro_message})