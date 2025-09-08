from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'acervo'

urlpatterns = [
    path('', views.acervo_view, name='acervo_view'),
    path('listar/', views.listar_imagens, name='listar_imagens'),
    path('upload/image', views.upload_imagem, name='upload_imagem'),
    path('upload/artigo/', views.upload_artigo, name='upload_artigo'),
    path('upload/link/', views.upload_link, name='upload_link'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]