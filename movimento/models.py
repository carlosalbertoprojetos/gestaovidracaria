from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from gestaovidracaria.constantes import STATUS_CHOICES, TYPE

from funcionario.models import Funcionario
from produto.models import Produto


class Movimento(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)
    operacao = models.CharField('Operação', max_length=6, choices=TYPE)
    data = models.DateField('Data')
    total = models.DecimalField(
        'Total', max_digits=11, decimal_places=2, null=True, blank=True, default=0)
    status = models.CharField(
        'Condição', max_length=10, choices=STATUS_CHOICES, default='pendente')
    local = models.CharField('Local', max_length=6)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'Movimentação de Estoque'
        verbose_name_plural = 'Movimentação de Estoque'

    def get_absolute_url_details(self):
        return reverse('order:order_details', args=[self.pk])

    def get_absolute_url_update(self):
        return reverse('order:order_update', args=[self.pk])

    def get_absolute_url_Editar(self):
        return reverse('pedidos:edit_order', args=[self.pk])

    def __str__(self):
        return str(self.id)


class ProdutoMovimento(models.Model):
    movimento = models.ForeignKey(Movimento, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, on_delete=models.DO_NOTHING, verbose_name='Produto'
    )
    quantidade = models.IntegerField('Quantidade', null=True)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2, default=0)
    detalhes = models.CharField('Detalhes', max_length=300, blank=True)
    subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, default=0)


@receiver(post_save, sender=ProdutoMovimento)
def inventory_delete(sender, instance, **kwargs):
    produto = Produto.objects.filter(pk=instance.produto_id)
    instance.subtotal = produto.quantidade * produto.preco
    instance.movimento.total += instance.subtotal
    instance.movimento.save()
        
    for p in produto:
        p.quant_produto -= instance.quantidade
        p.save()


@receiver(post_delete, sender=ProdutoMovimento)
def inventory_insert(sender, instance, **kwargs):
    produto = Produto.objects.filter(pk=instance.produto_id)
    for p in produto:
        p.quant_produto += instance.quantidade
        p.save()