from django.urls import path
from . import views

app_name = 'acervo'

urlpatterns = [
    path('', views.acervo_view, name='acervo_view'),
    path('listar/', views.listar_imagens, name='listar_imagens'),
    path('upload/', views.upload_imagem, name='upload_imagem'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
]