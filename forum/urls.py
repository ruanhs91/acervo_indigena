from django.urls import path 
from .views import TopicoList
from . import views


app_name = 'forum'

urlpatterns = [
    path('topicos/', TopicoList.as_view(), name='topicos'),
    path('topico/excluir/<int:pk>/', views.excluir_topico, name='excluir_topico'),
    path('topico/<int:id>/', views.detail_topico, name='detail_topico'),
    path('comentario/excluir/<int:pk>/', views.excluir_comentario, name='excluir_comentario'),
    path('reagir/<int:pk>/<str:tipo>/', views.reagir, name='reagir'),
]