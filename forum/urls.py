from django.urls import path 
from .views import TopicoList
from . import views


app_name = 'forum'

urlpatterns = [
    path('topicos/', TopicoList.as_view(), name='topicos'),
    path('topico/excluir/<int:pk>/', views.excluir_topico, name='excluir_topico'),
    path('topico/<int:pk>/', views.detail_topico, name='detail_topico'),
]