from django.db.models.signals import post_save 
from django.dispatch import receiver 
from acervo.models import Imagem, Artigos, Link, Videos, Audio
from .models import Topico

@receiver(post_save, sender=Imagem)
def criar_topico_img(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(titulo=f' {instance.titulo_img}', discussao=instance.discussao, autor=instance.enviado_usuario, imagem=instance)

@receiver(post_save, sender=Artigos)
def criar_topico_art(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(titulo=f' {instance.titulo_artigo}', discussao=instance.discussao, autor=instance.enviado_usuario,artigo=instance)

@receiver(post_save, sender=Link)
def criar_topico_url(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(titulo=f' {instance.titulo_link}', discussao=instance.discussao, autor=instance.enviado_usuario, link=instance)

@receiver(post_save, sender=Videos)
def criar_topico_vids(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(titulo=f' {instance.titulo_video}', discussao=instance.discussao, autor=instance.enviado_usuario, videos=instance)
        
@receiver(post_save, sender=Audio)
def criar_topico_audio(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(titulo=f' {instance.titulo_audio}', discussao=instance.discussao, autor=instance.enviado_usuario, audio=instance)



 