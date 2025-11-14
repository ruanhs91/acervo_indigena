from django import forms
from .models import Imagem, Artigos, Link, Videos, UsuarioAdaptado, Audio
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings 

class cadastroform(UserCreationForm): #formulário de cadastro
    class Meta:
        model = UsuarioAdaptado
        fields = ('first_name', 'username', 'email', 'password1', 'password2', 'nome_cidade', 'uf', 'foto_perfil')
        
    first_name = forms.CharField(required=True, label='Nome',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    nome_cidade = forms.CharField(required=False, label='Cidade', widget=forms.TextInput(attrs={'class': 'form-control'}))
    uf = forms.CharField(required=False, label='UF', widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2'}))
    foto_perfil = forms.ImageField(required=False, label='Foto de Perfil', widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))


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
        fields=['titulo_img', 'descricao_img', 'discussao', 'autor_img', 'imagem']
        widgets = {
            'titulo_img': forms.TextInput(attrs={'placeholder': 'Título da imagem','class': 'form-control'}),
            'descricao_img': forms.Textarea(attrs={'placeholder': 'Descrição da imagem','class': 'form-control', 'rows': 2}),
            'discussao': forms.Textarea(attrs={'placeholder': 'Escreva aqui o tópico da discussão...','class': 'form-control', 'rows': 2}),
            'autor_img': forms.TextInput(attrs={'placeholder':'Autor da imagem','class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
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
        fields=['titulo_artigo', 'descricao_artigo', 'discussao', 'autor_artigo', 'arquivo']
        widgets = {
            'titulo_artigo': forms.TextInput(attrs={'placeholder': 'Título do artigo','class': 'form-control'}),
            'descricao_artigo': forms.Textarea(attrs={'placeholder': 'Descrição do artigo','class': 'form-control', 'rows': 2}),
            'discussao': forms.Textarea(attrs={'placeholder': 'Escreva aqui o tópico da discussão...','class': 'form-control', 'rows': 2}),
            'autor_artigo': forms.TextInput(attrs={'placeholder': 'Autor do artigo','class': 'form-control'}),
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
        }
class LinkForm(forms.ModelForm):
    class Meta: 
        model = Link
        fields=['titulo_link', 'descricao_link', 'discussao','url', 'autor']
        widgets = {
            'titulo_link': forms.TextInput(attrs={'placeholder': 'Título do link','class': 'form-control'}),
            'descricao_link': forms.Textarea(attrs={'placeholder': 'Descrição do link','class': 'form-control', 'rows': 2}),
            'discussao': forms.Textarea(attrs={'placeholder': 'Escreva aqui o tópico da discussão...','class': 'form-control', 'rows': 2}),
            'url': forms.URLInput(attrs={'placeholder': 'Digite aqui a URL','class': 'form-control'}),
            'autor': forms.TextInput(attrs={'placeholder': 'Autor do link','class': 'form-control'}),
        }

class VideoForm(forms.ModelForm):
    class Meta: 
        model = Videos
        fields=['titulo_video', 'descricao_video', 'video', 'autor_video', 'discussao']
        widgets = {
            'titulo_video': forms.TextInput(attrs={'placeholder': 'Título do vídeo','class': 'form-control'}),
            'descricao_video': forms.Textarea(attrs={'placeholder': 'Descrição do vídeo','class': 'form-control', 'rows': 2}),
            'discussao': forms.Textarea(attrs={'placeholder': 'Escreva aqui o tópico de discussão...','class': 'form-control', 'rows': 2}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),
            'autor_video': forms.TextInput(attrs={'placeholder': 'Autor do vídeo','class': 'form-control'}),
        }
    
    def clean_video(self):
        video = self.cleaned_data.get('video')
        if video:
            if not video.name.endswith(('.mp4', '.mov', '.avi', '.mkv')):
                raise forms.ValidationError('Formato de vídeo não suportado.')
        return video

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['titulo_audio', 'descricao_audio', 'audio', 'autor_audio', 'discussao']
        widgets = {
            'titulo_audio': forms.TextInput(attrs={'placeholder': 'Título do áudio','class': 'form-control'}),
            'descricao_audio': forms.Textarea(attrs={'placeholder': 'Descrição do áudio','class': 'form-control', 'rows': 2}),
            'discussao': forms.Textarea(attrs={'placeholder': 'Escreva aqui o tópico de discussão...','class': 'form-control', 'rows': 2}),
            'audio': forms.FileInput(attrs={'class': 'form-control'}),
            'autor_audio': forms.TextInput(attrs={'placeholder': 'Autor do áudio','class': 'form-control'}),
        }

        def clean_audio(self):
            audio = self.cleaned_data.get('audio')
            if audio:
                if not audio.name.lower().endswith(('.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a')):
                    raise forms.ValidationError('Formato de áudio não suportado.')
            return audio

class PerfilForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=True),
        required=False,
        label="Nova Senha"
    )
    class Meta:
        model = UsuarioAdaptado
        fields = ['first_name', 'username', 'email', 'nome_cidade', 'uf', 'foto_perfil']
    
    def clean_username(self): #mensagem de erro user já existentee
        username = self.cleaned_data.get('username')
        if UsuarioAdaptado.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email') #mensagem de erro email já existente
        if UsuarioAdaptado.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este email já está cadastrado.")
        return email

