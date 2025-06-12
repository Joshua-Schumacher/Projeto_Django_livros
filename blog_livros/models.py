
from django.db import models
from django.utils import timezone

class Cadastro(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    apelido = models.CharField(max_length=20)
    senha = models.CharField(max_length=100)
     
    def __str__(self):
        """
        Método que retorna uma representação amigável do objeto Cliente.
        Isso é útil no painel administrativo do Django e ao depurar.
        """
        return f"{self.nome} {self.sobrenome})"
    
    class Meta:
        verbose_name = "Usuario"  
        verbose_name_plural = "Usuarios" 

class PostagemLivros(models.Model):
    autor_postagem = models.ForeignKey(
        Cadastro,                 # Relaciona com o Model Cliente
        on_delete=models.CASCADE, # O que fazer se o cliente for excluído: exclui a conta
        related_name='cadastro'    # Nome para acessar as contas a partir do cliente (ex: cliente.contas.all())
    )
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=25)
    
    genero = models.CharField(max_length=15)
    descricao = models.CharField(max_length=200)
    resenha = models.CharField(max_length=250)
    data_postagem = models.DateTimeField(default=timezone.now)

    """ def __str__(self):
        return f"{self.titulo} {self.autor}" """
    
    def __str__(self):
        # Usamos self.cliente.nome para acessar o nome do cliente relacionado
        return f"Autor {self.id} - {self.cadastro.nome} {self.cadastro.sobrenome}"

    class Meta:
        verbose_name = "Livro"  
        verbose_name_plural = "Livros" 

