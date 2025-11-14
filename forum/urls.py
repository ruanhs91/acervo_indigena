from django.urls import path 
from .views import TopicoList

app_name = 'forum'

urlpatterns = [
    path('topicos/', TopicoList.as_view(), name='topicos/'),
    
]