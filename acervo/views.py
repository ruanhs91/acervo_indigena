from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Imagem, Artigos, Link, Videos, UsuarioAdaptado
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from .forms import ImagemForm, cadastroform, LoginForm, ArtigoForm, LinkForm, VideoForm, PerfilForm, ImagemFiltroForm
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 

def login_view(request): #view de login
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
    context = {
        'form': form,
        'page': 'acervo',
    }
    return render(request, 'acervo/login.html', context)

def cadastro_view(request): #view de cadastro, ainda ajeitar
    if request.method == 'POST':
        form = cadastroform(request.POST)
        if form.is_valid():
            user = form.save()
            usuarios = Group.objects.get(name='Usuários')
            usuarios.user_set.add(user)
            return redirect('acervo:login')
    else:
        form = cadastroform()
    context = {
        'form': form,
        'page': 'acervo',
    }
    return render(request, 'acervo/cadastro.html', context)

def logout_view(request): #view de logout
    logout(request)
    return redirect('acervo:listar_imagens')

def listar_imagens(request): #view de listagem de imagens com filtro e paginação
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
        'page': 'acervo',
    }
    return render(request, "acervo/acervoimg.html", context)

def listar_artigos(request): #view de listagem de artigos, ajeitar 
    artigos = Artigos.objects.filter(aprovado='A').order_by('data_envio')
    context = {
        "artigos": artigos,
    }
    return render(request, "acervo/acervoarti.html", context)

def listar_links(request): #view de listagem de links, ajeitar
    links = Link.objects.filter(aprovado='A').order_by('data_envio')
    context = {
        "links": links,
    }
    return render(request, "acervo/acervolinks.html", context)

def listar_videos(request): #view de listagem de vídeos, ajeitar
    videos = Videos.objects.filter(aprovado='A').order_by('data_envio')
    context = {
        "videos": videos,
    }
    return render(request, "acervo/acervovids.html", context)

@login_required
def upload_imagem(request): #view de upload de imagem
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
    context = {
        'form': form,
        'page': 'acervo',
    }
    return render(request, "acervo/upload_imagem.html", context)

@login_required 
def upload_artigo(request): #view de upload de artigo
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = form.save(commit=False)
            arquivo.enviado_usuario = request.user 
            arquivo.save()
            return redirect('acervo:listar_imagens') #trocar por listar_artigos
    else:
        form = ArtigoForm()
    context = {
        'form': form,
        'page': 'acervo',
    }
    return render(request, 'acervo/upload_artigo.html', context)

@login_required 
def upload_link(request): #view de upload de link
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.enviado_usuario = request.user
            link.save()
            return redirect('acervo:listar_imagens') #trocar por listar_links
    else: 
        form = LinkForm()
    context = {
        'form': form,
        'page': 'acervo',
    }
    return render(request, 'acervo/upload_link.html', context)
    
def upload_video(request): #view de upload de vídeo
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
    context = {
        'form': form,
        'page': 'acervo',
    }
    return render(request, "acervo/upload_video.html", context)

def is_moderador(user): #checagem do grupo moderador
    return user.is_staff or user.groups.filter(name='Moderadores').exists()

@login_required
@user_passes_test(is_moderador) #exclusivo para moderadores e superusuários
def painel_moderacao(request): 
    imagens = Imagem.objects.filter(aprovado='P')
    artigos = Artigos.objects.filter(aprovado='P')
    links = Link.objects.filter(aprovado='P')
    videos = Videos.objects.filter(aprovado='P')
    return render(request, "acervo/painel_moderacao.html", {'imagens': imagens, 'artigos': artigos, 'links': links, 'videos': videos, 'page': 'acervo'})

@login_required
@user_passes_test(is_moderador)

def aprovar_conteudo(request, tipo, pk): #aprovação dos conteúdos do acervo aq
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
def rejeicao_conteudo(request, tipo, pk): #rejeição
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
def excluir_imagem(request,pk): #delete de imagem
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
    context = {
        'form': form,
        'imagem': imagem,
        'page': 'acervo',
    }
    return render(request, 'acervo/editar_imagem.html', context)

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
    context = {
        'form': form,
        'artigo': artigo,
        'page': 'acervo',
    }
    return render(request, 'acervo/editar_artigo.html', context)

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
    context = {
        'form': form,
        'link': link,
        'page': 'acervo',
    }
    return render(request, 'acervo/editar_link.html', context)

@login_required
@user_passes_test(is_moderador)
def excluir_link(request, pk):
    link = get_object_or_404(Link, pk=pk)
    link.delete()
    return redirect('acervo:listar_imagens') #trocar por listar_links

@login_required
def perfil_view(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.save()
            return redirect('acervo:listar_imagens')
    else:
        form = PerfilForm(instance=request.user)

    context = {
        'form': form,
        'page': 'acervo',
    }
    
    return render(request, 'acervo/perfil.html', context)

#gerenciamento de usuários 
def superuser_or_moderador(view_func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and (user.is_superuser or user.is_moderador()):
            return view_func(request, *args, **kwargs)
        return redirect('acervo:listar_imagens')
    return wrapper

@login_required
@superuser_or_moderador
def gerenciar_usuarios(request):
    busca = request.GET.get('busca', '')
    usuarios = UsuarioAdaptado.objects.all().order_by('-date_joined')

    if busca:
        usuarios = usuarios.filter(
            Q(username__icontains=busca) |
            Q(email__icontains=busca) |
            Q(first_name__icontains=busca)
        )

    paginator = Paginator(usuarios, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    querystring = f"busca={busca}" if busca else " "

    context = {
        'usuarios': page_obj,  
        'page_obj': page_obj,
        'busca': busca,
        'querystring': querystring,
        'page': 'acervo',
    }
    return render(request, 'acervo/gerenciar_usuarios.html', context)

@login_required
@superuser_or_moderador
def editar_tipo_usuario(request, user_id):
    usuario_editar = get_object_or_404(UsuarioAdaptado, id=user_id)
    grupos = {
        'usuario': Group.objects.get(name='Usuários'),
        'moderador': Group.objects.get(name='Moderadores'),
    }

    if request.user.is_moderador() and (usuario_editar.is_superuser or usuario_editar.is_moderador()):
        messages.error(request, "Moderadores não podem editar superusuários nem outros moderadores.")
        return redirect('acervo:gerenciar_usuarios')
    if usuario_editar == request.user:
        messages.error(request, "Você não pode alterar seu próprio tipo de usuário.")
        return redirect('acervo:gerenciar_usuarios')

    if request.method == 'POST':
        novo_tipo = request.POST.get('tipo_usuario')
        usuario_editar.groups.clear() 
        if novo_tipo == 'superuser' and request.user.is_superuser:
            usuario_editar.is_superuser = True
            usuario_editar.is_staff = True
            msg = "superusuário"

        elif novo_tipo == 'moderador':
            usuario_editar.is_superuser = False
            usuario_editar.is_staff = False
            usuario_editar.groups.add(grupos['moderador'])
            msg = "moderador"

        else:
            usuario_editar.is_superuser = False
            usuario_editar.is_staff = False
            usuario_editar.groups.add(grupos['usuario'])
            msg = "usuário comum"

        usuario_editar.save()
        messages.success(request, f"{usuario_editar.username} foi definido como {msg}.")
        return redirect('acervo:gerenciar_usuarios')

    return render(request, 'acervo/editar_cargo_usuario.html', {'usuario_editar': usuario_editar})

    