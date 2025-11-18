from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView #cbv
from .models import Topico 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class TopicoList(ListView):
    model = Topico 
    template_name = 'forum/lista_topicos.html'
    context_object_name = 'topicos'
    paginate_by = 10 
    ordering = ['-criado']

class TopicoDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Topico 
    template_name = 'forum/confirmar_delete.html'
    success_url = reverse_lazy('forum:lista_topicos')
    def test_func (self):
        user = self.request.user
        return (user.is_superuser or user.groups.filter(name='Moderadores').exists())

    


