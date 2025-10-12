from django import forms
from .models import Imagem, Artigos, Link, Videos
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings 

class cadastroform(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2')
        
    first_name = forms.CharField(required=True, label='Nome',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None 
    
        self.fields['username'].label = "Usuário"
        self.fields['password1'].label = "Senha"
        self.fields['password2'].label = 'Confirme a senha'

    

class LoginForm(AuthenticationForm): #formulário de login
    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
class ImagemForm(forms.ModelForm):
    class Meta: 
        model = Imagem
        fields=['titulo_img', 'descricao_img', 'autor_img', 'imagem']
        widgets = {
            'titulo_img': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_img': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'autor_img': forms.TextInput(attrs={'class': 'form-control'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
class ArtigoForm(forms.ModelForm):
    class Meta: 
        model = Artigos 
        fields=['titulo_artigo', 'descricao_artigo', 'autor_artigo', 'arquivo']
        widgets = {
            'titulo_artigo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_artigo': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'autor_artigo': forms.TextInput(attrs={'class': 'form-control'}),
            'arquivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
class LinkForm(forms.ModelForm):
    class Meta: 
        model = Link
        fields=['titulo_link', 'descricao_link', 'url']
        widgets = {
            'titulo_link': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_link': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class VideoForm(forms.ModelForm):
    class Meta: 
        model = Videos
        fields=['titulo_video', 'descricao_video', 'video']
        widgets = {
            'titulo_video': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_video': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    
    def clean_video(self):
        video = self.cleaned_data.get('video')
        if not video:
            raise forms.ValidationError('Envie um arquivo de vídeo.')

class PerfilForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('first_name', 'email')

