from decimal import Decimal
from django.db import models
from tourproject.constantes import STATUS_CHOICES, PGTO_CHOICES
from django.db.models.signals import post_save
from django.dispatch import receiver
import math

from fornecedor.models import Fornecedor
from banco.models import CaixaDia
from produto.models import Produto



class Compra(models.Model):
    data_compra = models.DateField('Data da Compra', null=True, blank=True)
    nota_fs = models.CharField('Nota Fiscal', max_length=15)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)    
    codigo = models.CharField('Código', max_length=30)       
    status_compra = models.CharField('Condição', max_length=10, choices=STATUS_CHOICES, default='pendente', blank=True)
    criadoem = models.DateTimeField(auto_now_add=True)
    atualizadoem = models.DateTimeField(auto_now=True)
    num_prestacoes = models.IntegerField('Número de prestações', null=True, default=0.0)
    total = models.DecimalField('Custo da Compra R$', max_digits=11, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras - Contas a Pagar'

    def __str__(self):
        return self.fornecedor.nome  


class CompraProduto(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='produtos')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto')
    quantidade = models.DecimalField('Quantidade',max_digits=10, decimal_places=3, default=0.0)
    preco = models.DecimalField('Valor de Compra', max_digits=10, decimal_places=2, default=0.0)
    detalhes = models.CharField('Detalhes da Venda', max_length=300, null=True, blank=True)
    status = models.CharField('Condição', max_length=10, choices=STATUS_CHOICES, default='pendente')
    subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = 'Produto da Compra'
        verbose_name_plural = 'Produtos da Compra'

    def __str__(self):
        return str(self.produto)


class CompraPrestacao(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='prestacoes')
    banco = models.ForeignKey(CaixaDia, on_delete=models.CASCADE)
    num_parcela = models.IntegerField('Número da Parcela', null=True, default=0.0)
    valor_parc = models.DecimalField('Valor da Parcela', max_digits=10, decimal_places=2, default=0.0)
    data_venc = models.DateField('Data de Vencimento')
    data_pgto = models.DateField('Data de Pagamento')
    status = models.BooleanField('Quitado', default=False)
    formapgto = models.CharField(
        'Forma pgto', max_length=11, choices=PGTO_CHOICES)
    juros = models.DecimalField('Juros %', max_digits=10, decimal_places=2, default=0.0, null=True, blank=True)
    parc_juros = models.DecimalField(max_digits=11, decimal_places=2, default=0.0)
    detalhes = models.CharField('Detalhes da Prestação', max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = 'Parcela da Compra'
        verbose_name_plural = 'Prestações da Compra' 

    def save(self, *args, **kwargs):
        juros = (self.juros/100)
        vparc = self.valor_parc
        vjuros = (vparc * juros)
        parc_juros = math.fsum([vparc, vjuros])
        self.parc_juros = Decimal(parc_juros)
        return super(CompraPrestacao, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.num_parcela) 


@receiver(post_save, sender=CompraPrestacao)
def comp_total_prestacoes_add(sender, instance, **kwargs):
    num_pres = CompraPrestacao.objects.filter(compra__id=instance.compra.id)
    instance.compra.num_prestacoes = num_pres.count()
    soma = 0
    for p in num_pres:
        soma += p.parc_juros
    instance.compra.total = soma
    instance.compra.save()