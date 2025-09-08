from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Imagem
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from .forms import ImagemForm, cadastroform, LoginForm, ArtigoForm, LinkForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('acervo:acervo_view')
            else:
                messages.error(request, "Usuário ou senha incorretos.⚠️")
        else:
            messages.error(request, "Usuário ou senha incorretos.⚠️")
    else:
        form=LoginForm()
    return render(request, 'acervo/login.html', {"form": form})

def cadastro_view(request):
    if request.method == 'POST':
        form = cadastroform(request.POST)
        if form.is_valid():
            user = form.save()
            usuarios = Group.objects.get(name='Usuários')
            usuarios.user_set.add(user)
            return redirect('acervo:login')
    else:
        form = cadastroform()
    return render(request, 'acervo/cadastro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('acervo:acervo_view')

def acervo_view(request):
    return render(request, 'acervo/acervoimg.html', {'page': 'acervo'})

def listar_imagens(request):
    imagens = Imagem.objects.all()
    return render(request, "acervo/acervoimg.html", {'imagens': imagens})

@login_required
def upload_imagem(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            imagem = form.save(commit=False)
            imagem.enviado_usuario = request.user
            imagem.save()
            return redirect('acervo:listar_imagens')
    else: 
        form = ImagemForm()
    return render(request, "acervo/upload_imagem.html", {'form': form})

@login_required 
def upload_artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = form.save(commit=False)
            arquivo.enviado_usuario = request.user 
            arquivo.save()
            return redirect('acervo:listar_imagens') #trocar por listar_artigos
    else:
        form = ArtigoForm()
    return render(request, 'acervo/upload_artigo.html', {'form': form})

@login_required 
def upload_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.enviado_usuario = request.user
            link.save()
            return redirect('acervo:listar_imagens') #trocar por listar_links
    else: 
        form = LinkForm()
        return render(request, 'acervo/upload_link.html', {'form': form})
    

