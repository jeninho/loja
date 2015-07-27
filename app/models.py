"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Produtos(models.Model):
    nome = models.CharField(max_length=45)
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    descricao = models.CharField(max_length=255)