from django.contrib import admin
from .models import Imagem, Link, Artigos, Videos, UsuarioAdaptado

@admin.register(UsuarioAdaptado)
class UsuarioAdaptadoAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "first_name", "is_staff", "is_active")
    search_fields = ("username", "email", "first_name")
    list_filter = ("is_staff", "is_active")

@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo_img", "enviado_usuario", "data_envio", "aprovado")
    list_filter = ("aprovado", "data_envio")
    search_fields = ("titulo_img", "descricao_img", "autor_img")
    list_editable = ("aprovado",)

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo_link", "url", "enviado_usuario", "data_envio", "aprovado")
    list_filter = ("aprovado", "data_envio")
    search_fields = ("titulo_link", "descricao_link", "autor")
    list_editable = ("aprovado",)
@admin.register(Artigos)
class ArtigosAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo_artigo", "enviado_usuario", "data_envio", "aprovado")
    list_filter = ("aprovado", "data_envio")
    search_fields = ("titulo_artigo", "descricao_artigo", "autor_artigo")
    list_editable = ("aprovado",)
@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo_video", "enviado_usuario", "data_envio", "aprovado")
    list_filter = ("aprovado", "data_envio")
    search_fields = ("titulo_video", "descricao_video", "autor_video")
    list_editable = ("aprovado",)