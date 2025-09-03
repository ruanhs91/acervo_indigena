from django.shortcuts import render, redirect
from .models import Imagem
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from .forms import ImagemForm, cadastroform, LoginForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('acervo:acervo_view')
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
    else:
        form = cadastroform()
    return render(request, 'acervo/cadastro.html', {'form': form})

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
            imagem.autor = request.user
            imagem.save()
            return redirect('acervo:listar_imagens')
    else: 
        form = ImagemForm()
    return render(request, "acervo/upload_imagem.html", {'form': form})

