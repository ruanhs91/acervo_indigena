from django.contrib import admin
from django.contrib.auth.models import Group

Group.objects.get_or_create(name='Moderadores')
# Register your models here.
