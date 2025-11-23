from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView #cbv
from .models import Topico 
from django.urls import reverse_lazy
from acervo.views import is_moderador

class TopicoList(ListView):
    model = Topico 
    template_name = 'forum/lista_topicos.html'
    context_object_name = 'topicos'
    paginate_by = 10 
    ordering = ['-criado']

@login_required
@user_passes_test(is_moderador)
def excluir_topico(request, pk):
    topico=get_object_or_404(Topico, id=pk)
    topico.delete()
    return redirect('forum:topicos')

def detail_topico(request, pk):
    topico = get_object_or_404(Topico, id=pk)
    context = {
        'topico': topico,
    }
    return render(request, 'forum/detalhe_topico.html', context)

