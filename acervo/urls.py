from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'acervo'

urlpatterns = [
    path('', views.listar_imagens, name='acervo_view'),
    path('listar/', views.listar_imagens, name='listar_imagens'),
    path('upload/image', views.upload_imagem, name='upload_imagem'),
    path('upload/artigo/', views.upload_artigo, name='upload_artigo'),
    path('upload/link/', views.upload_link, name='upload_link'),
    path('upload/video/', views.upload_video, name='upload_video'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('moderacao/', views.painel_moderacao, name='painel_moderacao'),
    path('moderacao/aprovar/<str:tipo>/<int:pk>/', views.aprovar_conteudo, name='aprovar_conteudo'),
    path('moderacao/rejeitar/<str:tipo>/<int:pk>/', views.rejeicao_conteudo, name='rejeicao_conteudo'),
    path('imagem/editar/<int:pk>/', views.editar_imagem, name='editar_imagem'),
    path('imagem/excluir/<int:pk>/', views.excluir_imagem, name='excluir_imagem'),
]