from decimal import Decimal
from django.db import models
from tourproject.constantes import STATUS_CHOICES, PGTO_CHOICES
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from client.models import Client
from banco.models import CaixaDia
from produto.models import Produto




class Venda(models.Model):
    data_venda = models.DateField()
    codigo = models.CharField(max_length=8)    
    nota_fs = models.CharField(max_length=10, blank=True)
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)    
    custo_total = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, default=0.0)
    desconto_venda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
    status_venda = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    num_parcelas = models.IntegerField(null=True, blank=True, default=0.0)
    vlr_parcelas = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas - Contas a Receber'

    def save(self, *args, **kwargs):
        vpacelas = Decimal(self.vlr_parcelas)
        # ctotal = Decimal(self.custo_total)
        desc = Decimal(self.desconto_venda/100)
        vlrdesc = vpacelas * desc
        total = vpacelas - vlrdesc
        self.custo_total = total
        return super(Venda, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.cliente.nome_contato


class VendaProduto(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='produtos')  
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto')
    quantidade = models.DecimalField('Quantidade', max_digits=10, decimal_places=2, default=0.0)
    preco = models.DecimalField('Valor de Venda', max_digits=10, decimal_places=2, default=0.0)
    detalhes = models.CharField('Detalhes da Venda', max_length=300, blank=True)   
    status = models.CharField('Condição', max_length=10, choices=STATUS_CHOICES, default='pendente')
    custo_venda = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = 'Produto da Venda'
        verbose_name_plural = 'Produtos da Venda'

    def __str__(self):
        return str(self.produto)


class VendaPrestacao(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='prestacoes')
    banco = models.ForeignKey(CaixaDia, on_delete=models.CASCADE, blank=True)
    num_parcela = models.IntegerField('Número da Parcela', blank=True, null=True, default=0.0)
    valor_parc = models.DecimalField('Valor das Parcelas R$', max_digits=10, decimal_places=2, default=0.0)
    formapgto = models.CharField(
        'Forma pgto', max_length=11, choices=PGTO_CHOICES, blank=True, null=True)
    data_venc = models.DateField('Data de Vencimento')
    data_pgto = models.DateField('Data de Pagamento')
    detalhes = models.CharField('Detalhes da Prestação', max_length=300, blank=True)
    status = models.BooleanField('Quitado', default=False) 

    class Meta:
        verbose_name = 'Parcela da Venda'
        verbose_name_plural = 'Prestações da Venda'

    def __str__(self):
        return str(self.num_parcela)


@receiver(post_save, sender=VendaPrestacao)
def comp_total_prestacoes_add(sender, instance, **kwargs):
    parcelas = VendaPrestacao.objects.filter(venda__id=instance.venda.id)
    instance.venda.num_parcelas = parcelas.count()
    soma = 0
    for p in parcelas:
        soma += p.valor_parc
    instance.venda.vlr_parcelas = soma
    instance.venda.save()