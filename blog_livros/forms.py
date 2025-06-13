from django import forms 
from .models import PostagemLivros, Cadastro
class PostagemForm(forms.ModelForm):
    class Meta:
        model = PostagemLivros 
        fields = [
            'titulo',
            'autor',
            'autor_postagem',
            'genero',
            'descricao',
            'resenha',
            'data_postagem',
        ]

        
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control","placeholder": "Título do livro"}),
            "autor": forms.TextInput(attrs={"class":"form-control","placeholder": "Nome do autor"}),
            "autor_postagem": forms.TextInput(attrs={"class": "form-control","placeholder": 'vazio....' }), 
            "data_postagem": forms.DateInput(attrs={"class": "form-control","placeholder": "DD/MM/AAAA", 'type': 'date'}), 
            "descricao": forms.TextInput(attrs={"class": "form-control","placeholder": "Resuma o enredo do livro"}),
            "resenha": forms.TextInput(attrs={"class": "form-control","placeholder": "Comente"}), 
            "genero": forms.TextInput(attrs={"class": "form-control","placeholder": "Ex: fantasia, romance,terror... "}), 
        }

class ContaForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = [
            'nome',
            'sobrenome',
            'email',
            'apelido',
            'senha',
        ]

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control","placeholder": "Digite seu nome"}),
            "sobrenome": forms.TextInput(attrs={"class":"form-control","placeholder": "Digite seu sobrenome"}),
            "email": forms.TextInput(attrs={"class": "form-control","placeholder": 'exemplo@gmail.com' }), 
            "apelido": forms.DateInput(attrs={"class": "form-control","placeholder": 'Nome de usuário'}), 
            "senha": forms.PasswordInput(attrs={"class": "form-control","placeholder": "Crie uma senha"}),
           
        }
        