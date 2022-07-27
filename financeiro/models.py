from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from gestaovidracaria.constantes import STATUS_CHOICES, PGTO_CHOICES


from produto.models import Produto
from cliente.models import Cliente
from fornecedor.models import Fornecedor



class Compra(models.Model):

    data = models.DateField('Data')
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.DO_NOTHING)
    formapgto = models.CharField(
        'Forma pgto', max_length=11, choices=PGTO_CHOICES)
    imagem = models.ImageField(upload_to='nfs_compras', blank=True, null=True)
    total = models.DecimalField(
        'Total', max_digits=11, decimal_places=2, null=True, blank=True, default=0)
    status = models.CharField(
        'Condição', max_length=10, choices=STATUS_CHOICES, default='pendente')

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class CompraProduto(models.Model):

    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, on_delete=models.DO_NOTHING, verbose_name='Produto'
    )
    quantidade = models.IntegerField('Quantidade', null=True)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, default=0)
    detalhes = models.CharField('Detalhes', max_length=300, blank=True)


class Venda(models.Model):

    data = models.DateField('Data')
    cliente = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING)
    num_venda = models.IntegerField('Nº Venda')
    formapgto = models.CharField(
        'Forma pgto', max_length=11, choices=PGTO_CHOICES)
    custo = models.DecimalField('Custo da venda', max_digits=10, decimal_places=2)
    total = models.DecimalField(
        'Total', max_digits=11, decimal_places=2, null=True, blank=True, default=0)
    status = models.CharField(
        'Condição', max_length=10, choices=STATUS_CHOICES, 
        default='pendente')

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'


@receiver(post_save, sender=Venda)
def estoque_venda(sender, instance, **kwargs):    
    produto = Produto.objects.filter(pk=instance.produto_id)

    for p in produto:
        p.estoque -= instance.quantidade
        p.save()
        instance.venda.total += instance.subtotal
        instance.venda.save()



class VendaProduto(models.Model):

    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, on_delete=models.DO_NOTHING, verbose_name='Produto'
    )
    quantidade = models.IntegerField('Quantidade', null=True)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    detalhes = models.CharField('Detalhes', max_length=300, blank=True)
    subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, default=0)