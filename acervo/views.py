from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Imagem, Artigos, Link, Videos, Perfil
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from .forms import ImagemForm, cadastroform, LoginForm, ArtigoForm, LinkForm, VideoForm, PerfilForm, ImagemFiltroForm
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 

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
    imagens = Imagem.objects.filter(aprovado='A').order_by('-data_envio')
    filtro_form = ImagemFiltroForm(request.GET or None)
    
    if filtro_form.is_valid():
        query = filtro_form.cleaned_data.get('query')
        data_inicio = filtro_form.cleaned_data.get('data_inicio')
        data_fim = filtro_form.cleaned_data.get('data_fim')

        if query:
            imagens = imagens.filter(
                Q(titulo_img__icontains=query) |
                Q(descricao_img__icontains=query) |
                Q(autor_img__icontains=query)
            )
        if data_inicio:
            imagens = imagens.filter(data_envio__date__gte=data_inicio)
        if data_fim:
            imagens = imagens.filter(data_envio__date__lte=data_fim)
    
    # paginação 

    itens_por_pagina = 9
    paginator = Paginator(imagens, itens_por_pagina)
    page_number = request.GET.get('page')

    params = request.GET.copy()
    if 'page' in params:
        params.pop('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger: 
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    context = {
        "imagens": page_obj,
        "page_obj": page_obj,
        'filtro_form': filtro_form,
        'querystring': params.urlencode(),
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
    
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.enviado_usuario = request.user
            video.aprovado ='P'
            video.save()
            return redirect('acervo:listar_imagens') #trocar por listar_videos
        else:
            messages.error(request, "Envie um arquivo em formato de vídeo.")
    else: 
        form = VideoForm()
    return render(request, "acervo/upload_video.html", {'form': form})

def is_moderador(user):
    return user.is_staff or user.groups.filter(name='Moderadores').exists()

@login_required
@user_passes_test(is_moderador)
def painel_moderacao(request):
    imagens = Imagem.objects.filter(aprovado='P')
    artigos = Artigos.objects.filter(aprovado='P')
    links = Link.objects.filter(aprovado='P')
    videos = Videos.objects.filter(aprovado='P')
    return render(request, "acervo/painel_moderacao.html", {'imagens': imagens, 'artigos': artigos, 'links': links, 'videos': videos})

@login_required
@user_passes_test(is_moderador)

def aprovar_conteudo(request, tipo, pk):
    if tipo == "imagem":
        conteudo = get_object_or_404(Imagem, pk=pk)
    elif tipo == "artigo":
        conteudo = get_object_or_404(Artigos, pk=pk)
    elif tipo == "link":
        conteudo = get_object_or_404(Link, pk=pk)
    elif tipo == "video":
        conteudo = get_object_or_404(Videos, pk=pk)
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
    elif tipo == "video":
        conteudo = get_object_or_404(Videos, pk=pk)
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
    artigo = get_object_or_404(Artigos, pk=pk)
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

@login_required
def perfil_view(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.save()
            if 'foto_perfil' in request.FILES:
                perfil, created = Perfil.objects.get_or_create(user=user)
                perfil.foto_perfil = request.FILES['foto_perfil']
                perfil.save()
            
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('acervo:listar_imagens')
    else:
        form = PerfilForm(instance=request.user)
    
    return render(request, 'acervo/perfil.html', {'form': form})