from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Imagem, Artigos, Link
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from .forms import ImagemForm, cadastroform, LoginForm, ArtigoForm, LinkForm
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.db.models import Q

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('acervo:listar_imagens')
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
    return redirect('acervo:listar_imagens')

def listar_imagens(request):
    query = request.GET.get('q')
    imagens = Imagem.objects.filter(aprovado='A')

    if query:
        imagens = imagens.filter(Q(titulo_img__icontains=query) | Q(descricao_img__icontains=query) | Q(autor_img__icontains=query))

    context = {
        "imagens": imagens,
        "query": query,
    }
    return render(request, "acervo/acervoimg.html", context)

@login_required
def upload_imagem(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            imagem = form.save(commit=False)
            imagem.enviado_usuario = request.user
            imagem.aprovado ='P'
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
    

def is_moderador(user):
    return user.is_staff or user.groups.filter(name='Moderadores').exists()

@login_required
@user_passes_test(is_moderador)
def painel_moderacao(request):
    imagens = Imagem.objects.filter(aprovado='P')
    artigos = Artigos.objects.filter(aprovado='P')
    links = Link.objects.filter(aprovado='P')

    return render(request, "acervo/painel_moderacao.html", {'imagens': imagens, 'artigos': artigos, 'links': links})

@login_required
@user_passes_test(is_moderador)

def aprovar_conteudo(request, tipo, pk):
    if tipo == "imagem":
        conteudo = get_object_or_404(Imagem, pk=pk)
    elif tipo == "artigo":
        conteudo = get_object_or_404(Artigos, pk=pk)
    elif tipo == "link":
        conteudo = get_object_or_404(Link, pk=pk)
    else:
        return redirect('acervo:painel_moderacao')
    
    conteudo.aprovado = 'A' 
    conteudo.save()
    return redirect('acervo:painel_moderacao')

@login_required
@user_passes_test(is_moderador)
def rejeicao_conteudo(request, tipo, pk):
    if tipo == "imagem":
        conteudo = get_object_or_404(Imagem, pk=pk)
    elif tipo == "artigo":
        conteudo = get_object_or_404(Artigos, pk=pk)
    elif tipo == "link":
        conteudo = get_object_or_404(Link, pk=pk)
    else:
        return redirect('acervo:painel_moderacao')
    
    conteudo.aprovado = 'R'
    conteudo.save()
    return redirect('acervo:painel_moderacao')

@login_required
@user_passes_test(is_moderador)
def excluir_imagem(request,pk):
    imagem = get_object_or_404(Imagem, pk=pk)
    imagem.delete()
    return redirect('acervo:listar_imagens')

@login_required 
@user_passes_test(is_moderador)
def editar_imagem(request, pk):
    imagem = get_object_or_404(Imagem, pk=pk)
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES, instance=imagem)
        if form.is_valid():
            form.save()
            return redirect('acervo:listar_imagens')
    else:
        form = ImagemForm(instance=imagem)
    return render(request, 'acervo/editar_imagem.html', {'form': form, 'imagem': imagem})

@login_required 
@user_passes_test(is_moderador)
def editar_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('acervo:listar_imagens') #trocar por listar_artigos
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'acervo/editar_artigo.html', {'form': form, 'artigo': artigo})

@login_required
@user_passes_test(is_moderador)
def excluir_artigo(request, pk):
    artigo = get_object_or_404(Artigos, pk=pk)
    artigo.delete()
    return redirect('acervo:listar_imagens') #trocar por listar_artigos

@login_required
@user_passes_test(is_moderador)
def editar_link(request, pk):
    link = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            return redirect('acervo:listar_imagens') #trocar por listar_links
    else:
        form = LinkForm(instance=link)
    return render(request, 'acervo/editar_link.html', {'form': form, 'link': link})

@login_required
@user_passes_test(is_moderador)
def excluir_link(request, pk):
    link = get_object_or_404(Link, pk=pk)
    link.delete()
    return redirect('acervo:listar_imagens') #trocar por listar_links

