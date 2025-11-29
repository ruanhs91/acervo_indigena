from django import forms
from .models import Comentario 

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario 
        fields = ['coment']
        widgets = {
            'coment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escreva seu comentário aqui...'}),
        }
        