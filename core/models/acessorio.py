from django.db import models

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)
    categoria = models.ForeignKey('core.Categoria', on_delete=models.CASCADE, default=1)
    cor = models.ForeignKey('core.Cor', on_delete=models.CASCADE,  default=1)
    marca = models.ForeignKey('core.Marca', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.descricao} ({self.id})"

class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    acessorios = models.ManyToManyField('Acessorio', related_name='veiculos')
    
    def __str__(self):
        return self.modelo
