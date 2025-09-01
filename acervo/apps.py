from django.apps import AppConfig


class AcervoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'acervo'

    def ready(self):
        from django.contrib.auth.models import Group
        for nome in ('Usuários', 'Moderadores'):
            Group.objects.get_or_create(name = nome)
            
