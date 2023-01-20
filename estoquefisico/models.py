from django.db import models
from django.db import connection
from django.urls import reverse
import locale
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from django.core.exceptions import ValidationError

from produto.models import Produto


#VALIDA CAMPOS

def validate_campos(value):
    if not value.isdigit():
        raise ValidationError('O campo deve conter apenas números')
#==================================================================================================

#ESTOQUE FÍSICO

class EstoqueFisico(models.Model):
    
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)    
    estoque_atual = models.DecimalField('Estoque Atual', max_digits=10, decimal_places=2, default=0.0)
    #estoque_final = models.DecimalField('Estoque Final', max_digits=10, decimal_places=2, default=0.0)
    status = models.BooleanField('Disponível', default=True)    
    data_creat = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)

    class Meta:        
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"      

    def __str__(self):
        return f'{self.produto.nome}'
