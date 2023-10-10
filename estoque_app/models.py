from django.db import models

# Create your models here.
class Estoque(models.Model):
    id_uni = models.AutoField(primary_key=True)
    alimento = models.TextField(max_length=255)
    quantidade_qtd = models.FloatField()
    validade = models.DateField()
    porcao = models.IntegerField(default=1)
    
   


