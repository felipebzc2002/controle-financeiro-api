from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Transacao(models.Model):
    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    tipo = (
        ("ENTRADA", "Entrada"),
        ("SAÍDA", "Saída")
    )
    tipo_de_transacao = models.CharField( max_length=50, choices= tipo, default= "ENTRADA")
    data = models.DateTimeField(auto_now_add= True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descricao