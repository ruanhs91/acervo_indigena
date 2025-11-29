from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'acervo'

urlpatterns = [
    path('', views.listar_imagens, name='acervo_view'),
    path('listar/', views.listar_imagens, name='listar_imagens'),
    path('listar/artigos/', views.listar_artigos, name='listar_artigos'),
    path('listar/links/', views.listar_links, name='listar_links'),
    path('listar/videos/', views.listar_videos, name='listar_videos'),
    path('listar/audios/', views.listar_audios, name='listar_audios'),
    path('upload/image', views.upload_imagem, name='upload_imagem'),
    path('upload/artigo/', views.upload_artigo, name='upload_artigo'),
    path('upload/link/', views.upload_link, name='upload_link'),
    path('upload/video/', views.upload_video, name='upload_video'),
    path('upload/audio/', views.upload_audio, name='upload_audio'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('moderacao/', views.painel_moderacao, name='painel_moderacao'),
    path('moderacao/aprovar/<str:tipo>/<int:pk>/', views.aprovar_conteudo, name='aprovar_conteudo'),
    path('moderacao/rejeitar/<str:tipo>/<int:pk>/', views.rejeicao_conteudo, name='rejeicao_conteudo'),
    path('imagem/editar/<int:pk>/', views.editar_imagem, name='editar_imagem'),
    path('imagem/excluir/<int:pk>/', views.excluir_imagem, name='excluir_imagem'),
    path('artigo/editar/<int:pk>/', views.editar_artigo, name='editar_artigo'),
    path('artigo/excluir/<int:pk>/', views.excluir_artigo, name='excluir_artigo'),
    path('audio/editar/<int:pk>/', views.editar_audio, name='editar_audio'),
    path('audio/excluir/<int:pk>/', views.excluir_audio, name='excluir_audio'),
    path('video/editar/<int:pk>/', views.editar_video, name='editar_video'),
    path('video/excluir/<int:pk>/', views.excluir_video, name='excluir_video'),
    path('link/editar/<int:pk>/', views.editar_link, name='editar_link'),
    path('link/excluir/<int:pk>/', views.excluir_link, name='excluir_link'),
    path('gerenciar_usuarios/', views.gerenciar_usuarios, name='gerenciar_usuarios'),
    path('editar_usuario/<int:user_id>/', views.editar_tipo_usuario, name='editar_tipo_usuario'),
]