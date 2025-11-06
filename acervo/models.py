from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioAdaptado(AbstractUser):
    nome_cidade = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to="acervo/perfil/", blank=True, null=True)

    def __str__(self):
        return self.username
    
    def is_moderador(self):
        return self.groups.filter(name='Moderadores').exists()
    def is_usuario_comum(self):
        return self.groups.filter(name='Usuários').exists()

class Imagem(models.Model):
    titulo_img = models.CharField(max_length=200)
    descricao_img = models.TextField()
    imagem = models.ImageField(upload_to="acervo/acervoimg/")
    enviado_usuario = models.ForeignKey(UsuarioAdaptado, on_delete=models.CASCADE, blank=True, null=True)
    data_envio = models.DateTimeField(auto_now_add=True)
    autor_img=models.CharField(max_length=100, blank=True)
    aprovado_opcoes = [
        ('P', 'Pendente'),
        ('A', 'Aprovado'),
        ('R', 'Rejeitado'),
    ]
    aprovado = models.CharField(max_length=1, choices=aprovado_opcoes, default='P')

    def __str__(self):
        return self.titulo_img

class Link(models.Model):
    url = models.URLField(max_length=200)
    descricao_link = models.TextField()
    titulo_link = models.CharField(max_length=200)
    enviado_usuario = models.ForeignKey(UsuarioAdaptado, on_delete=models.CASCADE, blank=True, null=True)
    data_envio = models.DateTimeField(auto_now_add=True)
    autor=models.CharField(max_length=100, blank=True, null=True)
    aprovado_opcoes = [
        ('P', 'Pendente'),
        ('A', 'Aprovado'),
        ('R', 'Rejeitado'),
    ]
    aprovado = models.CharField(max_length=1, choices=aprovado_opcoes, default='P')

    def __str__(self):
        return self.titulo_link

class Artigos(models.Model):
    titulo_artigo = models.CharField(max_length=200)
    descricao_artigo = models.TextField()
    arquivo = models.FileField(upload_to="acervo/artigos/")
    enviado_usuario = models.ForeignKey(UsuarioAdaptado, on_delete=models.CASCADE, blank=True, null=True)
    data_envio = models.DateTimeField(auto_now_add=True)
    autor_artigo=models.CharField(max_length=100, blank=True)
    aprovado_opcoes = [
        ('P', 'Pendente'),
        ('A', 'Aprovado'),
        ('R', 'Rejeitado'),
    ]
    aprovado = models.CharField(max_length=1, choices=aprovado_opcoes, default='P')

    def __str__(self):
        return self.titulo_artigo
    
class Videos(models.Model):
    titulo_video = models.CharField(max_length=200)
    descricao_video = models.TextField()
    video = models.FileField(upload_to="acervo/videos/")
    enviado_usuario = models.ForeignKey(UsuarioAdaptado, on_delete=models.CASCADE, blank=True, null=True)
    data_envio = models.DateTimeField(auto_now_add=True)
    autor_video=models.CharField(max_length=100, blank=True, null=True)
    aprovado_opcoes = [
        ('P', 'Pendente'),
        ('A', 'Aprovado'),
        ('R', 'Rejeitado'),
    ]
    aprovado = models.CharField(max_length=1, choices=aprovado_opcoes, default='P')

    def __str__(self):
        return self.titulo_video


    
