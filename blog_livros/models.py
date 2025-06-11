from django.db import models
from django.utils import timezone

class PostagemLivros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=25)
    autor_postagem = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=15)
    descricao = models.CharField(max_length=200)
    resenha = models.CharField(max_length=250)
    data_postagem = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.titulo} {self.autor}"


class Meta:
    verbose_name = "Livro"  
    verbose_name_plural = "Livros" 

class Cadastro(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    apelido = models.CharField(max_length=20)
    senha = models.CharField(max_length=100)


