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
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'Movimento'
        verbose_name_plural = 'Movimento'

    # def get_absolute_url_client_list(self):
    #     return reverse('order:orders_client_list', args=[self.client.pk])

    def get_absolute_url_details(self):
        return reverse('order:order_details', args=[self.pk])

    def get_absolute_url_update(self):
        return reverse('order:order_update', args=[self.pk])

    def get_absolute_url_Editar(self):
        return reverse('pedidos:edit_order', args=[self.pk])

    # def get_absolute_url_Orcamento(self):
    #     return reverse('pedidos:orcamento', args=[self.int:cliente.id]/[self.pk])

    # def print(self):
    #     return mark_safe("""<a href=\"{% url 'order:budget' self.pk %} \"target="_blank">
    #     <img src=\"/static/produtos/b_print.png\"></a>""")

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=Movimento)
def movimento_estoque(sender, instance, **kwargs):    
    produto = Produto.objects.filter(movimento_id=instance.id)
    for p in produto:
        if instance.operacao == 'Compra':
            p.estoque += instance.quantidade
        else:
            p.estoque -= instance.quantidade
        p.save()
        instance.total += instance.subtotal
        instance.save()


class ProdutoMovimento(models.Model):

    movimento = models.ForeignKey(Movimento, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, on_delete=models.DO_NOTHING, verbose_name='Produto'
    )
    quantidade = models.IntegerField('Quantidade', null=True)
    preço = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    detalhes = models.CharField('Detalhes', max_length=300, blank=True)
    subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, default=0)


@receiver(post_save, sender=ProdutoMovimento)
def inventory_delete(sender, instance, **kwargs):
    produto = Produto.objects.filter(pk=instance.produto_id)
    instance.subtotal = instance.preço * instance.quantidade
    instance.movimento.total += instance.subtotal
    instance.movimento.save()
        
    for p in produto:
        p.estoque -= instance.quantidade
        p.save()


@receiver(post_delete, sender=ProdutoMovimento)
def inventory_insert(sender, instance, **kwargs):
    produto = Produto.objects.filter(pk=instance.produto_id)
    for p in produto:
        p.estoque += instance.quantidade
        p.save()


"""
    # def __str__(self):
    #     return str(self.produto)
        # return str(self.order.client) + ",R$" + str(self.price) + "," + str(self.amount) + ",R$" + str(self.subtotal)

    # calculo
    # def save(self, *args, **kwargs):
    #     self.subtotal = self.preço * self.quantidade
    #     self.movimento.total += self.subtotal
    #     self.movimento.save()
    #     return super(ProdutoMovimento, self).save(*args, **kwargs)
"""
