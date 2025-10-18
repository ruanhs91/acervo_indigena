from django import forms
from .models import Imagem, Artigos, Link, Videos, Perfil
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings 

class cadastroform(UserCreationForm): #formulário de cadastro
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2')
        
    first_name = forms.CharField(required=True, label='Nome',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    def __init__(self, *args, **kwargs): # lembrar de botar pra n cadastrar mais de um email igual
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
class ImagemFiltroForm(forms.Form):
    query = forms.CharField(
        required=False, widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Buscar por título, descrição ou autor...'}),
            label='Título, descrição ou autor'
        )
    data_inicio = forms.DateField(
        required=False, widget=forms.DateInput(attrs={
            'class':'form-control',
            'type':'date'}),
            label='Data Início'
        )
    data_fim = forms.DateField(
        required=False, widget=forms.DateInput(attrs={
            'class':'form-control',
            'type':'date'}),
            label='Data Fim'
    )
    
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
        fields=['titulo_link', 'descricao_link', 'url', 'autor']
        widgets = {
            'titulo_link': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_link': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
        }

class VideoForm(forms.ModelForm):
    class Meta: 
        model = Videos
        fields=['titulo_video', 'descricao_video', 'video', 'autor_video']
        widgets = {
            'titulo_video': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_video': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'autor_video': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def clean_video(self):
        video = self.cleaned_data.get('video')
        if video:
            if not video.name.endswith(('.mp4', '.mov', '.avi', '.mkv')):
                raise forms.ValidationError('Formato de vídeo não suportado.')
        return video


class PerfilForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=True),
        required=False,
        label="Nova Senha")
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']
    
    def clean_username(self): #mensagem de erro user já existentee
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email') #mensagem de erro email já existente
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este email já está cadastrado.")
        return email

