from django.db import models
from acervo.models import UsuarioAdaptado, Imagem, Artigos, Link, Videos, Audio

class Topico(models.Model):
    titulo = models.CharField(max_length=250)
    autor = models.ForeignKey(UsuarioAdaptado, on_delete=models.CASCADE)
    descricao = models.TextField(default='',max_length=500, blank=True)
    autor_nome = models.CharField(default='',max_length=100, blank=True)
    criado= models.DateTimeField(auto_now_add=True)
    discussao = models.TextField(default='', max_length=2000)
    imagem = models.OneToOneField(Imagem, on_delete=models.CASCADE, null=True, blank=True)
    artigo = models.OneToOneField(Artigos, on_delete=models.CASCADE, null=True, blank=True)
    link = models.OneToOneField(Link, on_delete=models.CASCADE, null = True, blank = True)
    videos = models.OneToOneField(Videos, on_delete=models.CASCADE, null = True, blank=True)
    audio = models.OneToOneField(Audio, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.titulo 

    class Meta:
        ordering = ['criado']

class Reagir(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, related_name='reacoes')
    usuario = models.ForeignKey(UsuarioAdaptado, on_delete=models.CASCADE)
    LIKE = 'like'
    DESLIKE = 'deslike'
    TIPO_REACAO = [
        (LIKE, 'Like'),
        (DESLIKE, 'Deslike'),
    ]
    tipo = models.CharField(max_length=7, choices=TIPO_REACAO)

    class Meta:
        unique_together = ('topico', 'usuario')
class Comentario(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(UsuarioAdaptado, on_delete=models.CASCADE)
    coment = models.TextField()
    criado = models.DateTimeField(auto_now_add=True)
    #respostas
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='respostas')

    def __str__(self):
        return self.topico 
    
    class Meta:
        ordering = ['criado']
    @property    
    def is_resposta(self):
        return self.parent is not None 

