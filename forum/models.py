from django.db import models
from acervo.models import UsuarioAdaptado, Imagem, Artigos, Link, Videos

class Topico(models.Model):
    titulo = models.CharField(max_length=250)
    autor = models.ForeignKey(UsuarioAdaptado, on_delete=models.CASCADE)
    criado= models.DateTimeField(auto_now_add=True)
    discussao = models.TextField(default='', max_length=2000)
    imagem = models.OneToOneField(Imagem, on_delete=models.CASCADE, null=True, blank=True)
    artigo = models.OneToOneField(Artigos, on_delete=models.CASCADE, null=True, blank=True)
    link = models.OneToOneField(Link, on_delete=models.CASCADE, null = True, blank = True)
    videos = models.OneToOneField(Videos, on_delete=models.CASCADE, null = True, blank=True)
    def __str__(self):
        return self.titulo 

    class Meta:
        ordering = ['criado']

class Comentario(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    autor = models.ForeignKey(UsuarioAdaptado, on_delete=models.CASCADE)
    coment = models.TextField()
    criado = models.DateTimeField(auto_now_add=True)
    #respostas
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.topico 
    
    class Meta:
        ordering = ['criado']
    @property    
    def is_resposta(self):
        return self.parent is not None 

