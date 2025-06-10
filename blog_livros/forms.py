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
            "genero": forms.EmailInput(attrs={"class": "form-control","placeholder": "Ex: fantasia, romance,terror... "}), 
        }

class ContaForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = [
            'titulo',
            'autor',
            'autor_postagem',
            'genero',
            'descricao',
            'resenha',
            'data_postagem',
        ]

