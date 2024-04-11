from django.db import models
from uploader.models import Image


class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)
    categoria = models.ForeignKey('core.Categoria', on_delete=models.CASCADE, default=1)
    cor = models.ForeignKey('core.Cor', on_delete=models.CASCADE,  default=1)
    marca = models.ForeignKey('core.Marca', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.descricao} ({self.id})"

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    acessorios = models.ManyToManyField('Acessorio', related_name='carros')
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.modelo
