from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView
from .models import Topico, Comentario, UsuarioAdaptado, Reagir
from acervo.views import is_moderador
from .forms import ComentarioForm
from django.contrib import messages


class TopicoList(ListView):
    model = Topico
    template_name = 'forum/lista_topicos.html'
    context_object_name = 'topicos'
    paginate_by = 10
    ordering = ['-criado']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for t in context["topicos"]:
            t.likes = t.reacoes.filter(tipo="like").count()
            t.deslikes = t.reacoes.filter(tipo="dislike").count()

        return context

@login_required
@user_passes_test(is_moderador)
def excluir_topico(request, pk):
    topico = get_object_or_404(Topico, id=pk)
    topico.delete()
    return redirect('forum:topicos')

def detail_topico(request, id):
    topico = get_object_or_404(Topico, id=id)
    comentarios = Comentario.objects.filter(topico=topico)

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            novo = form.save(commit=False)

            try:
                usuario_adaptado = request.user
            except UsuarioAdaptado.DoesNotExist:
                messages.error(request, "Conta inválida para postar comentário.")
                return redirect('forum:detail_topico', id=id)


            novo.autor = usuario_adaptado
            novo.topico = topico
            novo.save()

            messages.success(request, "Comentário enviado!")
            return redirect('forum:detail_topico', id=id)

    else:
        form = ComentarioForm()

    return render(request, "forum/detalhe_topico.html", {
        "topico": topico,
        "comentarios": comentarios,
        "form": form
    })

@login_required
def excluir_comentario(request, pk):
    comentario = get_object_or_404(Comentario, id=pk)

    if not (
        comentario.autor == request.user 
        or request.user.is_staff 
        or request.user.is_superuser 
        or request.user.is_moderador()
    ):
        messages.error(request, "Você não tem permissão para excluir este comentário.")
        return redirect('forum:detail_topico', id=comentario.topico.id)

    topico_id = comentario.topico.id
    comentario.delete()
    messages.success(request, "Comentário excluído com sucesso!")

    return redirect('forum:detail_topico', id=topico_id)


@login_required
def reagir(request, pk, tipo):
    topico = get_object_or_404(Topico, pk=pk)

    if tipo not in ["like", "dislike"]:
        return redirect("forum:topicos")

    reacao_existente = Reagir.objects.filter(usuario=request.user, topico=topico).first()

    if reacao_existente:
        if reacao_existente.tipo == tipo:
            reacao_existente.delete()  
        else:
            reacao_existente.tipo = tipo
            reacao_existente.save()
    else:
        Reagir.objects.create(usuario=request.user, topico=topico, tipo=tipo)

    return redirect("forum:topicos")

