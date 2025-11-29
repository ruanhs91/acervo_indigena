from django.db.models.signals import post_save 
from django.dispatch import receiver 
from acervo.models import Imagem, Artigos, Link, Videos, Audio
from .models import Topico

@receiver(post_save, sender=Imagem)
def criar_topico_img(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(
            titulo=instance.titulo_img,
            discussao=instance.discussao,
            descricao=instance.descricao_img,     
            autor=instance.enviado_usuario,       
            autor_nome=instance.autor_img,        
            imagem=instance
        )
@receiver(post_save, sender=Artigos)
def criar_topico_art(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(
            titulo=instance.titulo_artigo,
            discussao=instance.discussao,
            descricao=instance.descricao_artigo,  
            autor=instance.enviado_usuario,
            autor_nome=instance.autor_artigo,     
            artigo=instance
        )
@receiver(post_save, sender=Link)
def criar_topico_url(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(
            titulo=instance.titulo_link,
            discussao=instance.discussao,
            descricao=instance.descricao_link,   
            autor=instance.enviado_usuario,
            autor_nome=instance.autor,         
            link=instance
        )
@receiver(post_save, sender=Videos)
def criar_topico_vids(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(
            titulo=instance.titulo_video,
            discussao=instance.discussao,
            descricao=instance.descricao_video,  
            autor=instance.enviado_usuario,
            autor_nome=instance.autor_video,      
            videos=instance
        )
@receiver(post_save, sender=Audio)
def criar_topico_audio(sender, instance, created, **kwargs):
    if created:
        Topico.objects.create(
            titulo=instance.titulo_audio,
            discussao=instance.discussao,
            descricao=instance.descricao_audio,  
            autor=instance.enviado_usuario,
            autor_nome=instance.autor_audio,      
            audio=instance
        )
