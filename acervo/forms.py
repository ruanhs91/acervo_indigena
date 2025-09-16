from django import forms
from .models import Imagem, Artigos, Link
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings 

class cadastroform(UserCreationForm): #formulário de cadastro 
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=True, label='Nome')

    class Meta: 
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),

        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None 
    
        self.fields['username'].label = "Usuário"
        self.fields['password1'].label = "Senha"
        self.fields['password2'].label = 'Confirme a senha'


    def save (self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        if commit: 
            user.save()
        return user
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Insira um email válido.")

class LoginForm(AuthenticationForm): #formulário de login
    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
class ImagemForm(forms.ModelForm):
    class Meta: 
        model = Imagem
        fields=['titulo_img', 'descricao_img', 'autor_img', 'imagem']

class ArtigoForm(forms.ModelForm):
    class Meta: 
        model = Artigos 
        fields=['titulo_artigo', 'descricao_artigo', 'autor_artigo', 'arquivo']

class LinkForm(forms.ModelForm):
    class Meta: 
        model = Link
        fields=['titulo_link', 'descricao_link', 'url']
        

    
