from django.db import models

# Create your models here.

class Servico(models.Model):
    nome = models.CharField(max_length=80)
    valor = models.FloatField()
    disponivel = models.BooleanField()