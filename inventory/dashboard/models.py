from django.db import models
from django.contrib.auth.models import User

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
    
    class Meta:
        verbose_name_plural = 'Product'
    
    def __str__(self):
        return f'{self.nome} - {self.quantidade}'
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Order'
    
    def __str__(self):
        return f'{self.product} ordered by {self.staff}'
