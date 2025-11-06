from django.db.models.signals import post_save 
from django.dispatch import receiver 
from acervo.models import Imagem, Artigos, Link, Videos
from .models import Topico

@receiver(post_save, sender=Imagem)
def criar_topico_img(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(titulo=f'Discussão: {instance.titulo_img}', autor=instance.enviado_usuario, imagem=instance)

@receiver(post_save, sender=Artigos)
def criar_topico_art(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(titulo=f'Discussão: {instance.titulo_artigo}', autor=instance.enviado_usuario, artigo=instance)

@receiver(post_save, sender=Link)
def criar_topico_url(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(titulo=f'Discussão: {instance.titulo_link}', autor=instance.enviado_usuario, link=instance)

@receiver(post_save, sender=Videos)
def criar_topico_vids(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(titulo=f'Discussão: {instance.titulo_video}', autor=instance.enviado_usuario, videos=instance)




 