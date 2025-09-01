from django.db import models
from django.contrib.auth.models import User

class Imagem(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="acervo/acervoimg/")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
# Create your models here.
