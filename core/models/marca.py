from django.db import models

class MArca(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome.upper()