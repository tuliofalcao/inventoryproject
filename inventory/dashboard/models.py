from django.db import models

# Create your models here.

CATEGORIA = {
    ('Estacionario','Estacionario'),
    ('Eletronicos','Eletronicos'),
    ('Alimento','Alimento'),
}


class Product(models.Model):
    nome = models.CharField(max_length=100, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA, null=True)
    quantidade = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return f'{self.nome} - {self.quantidade}'
