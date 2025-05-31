from django.db import models

class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=25)
    genero = models.CharField(max_length=15)
    descricao = models.CharField(max_length=200)
    resenha = models.CharField(max_length=250)
    data_postagem = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.titulo} {self.autor}"


class Meta:
    verbose_name = "Livro"  
    verbose_name_plural = "Livros" 