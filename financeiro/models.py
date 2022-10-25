from django.db import models
from django.utils.formats import number_format
from gestaovidracaria.constantes import STATUS_CHOICES, PGTO_CHOICES
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from produto.models import Produto
from cliente.models import Cliente
from fornecedor.models import Fornecedor


class Compra(models.Model):
    codigo = models.CharField('Código da Compra', max_length=10)
    data = models.DateField('Data da Compra')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    formapgto = models.CharField('Forma de Pagamento', max_length=11, choices=PGTO_CHOICES)
    imagem = models.ImageField(upload_to='nfs_compras', blank=True, null=True)
    total = models.DecimalField('Total da Compra', max_digits=11, decimal_places=2, null=True, blank=True, default=0)
    status = models.CharField('Condição', max_length=10, choices=STATUS_CHOICES, default='pendente')

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def totalCompra(self):
        return "R$ %s" % number_format(self.total, 2)

    def __str__(self) -> str:
        return f'{self.fornecedor} - {self.data.day}/{self.data.month}/{self.data.year}'  


class CompraProduto(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, on_delete=models.DO_NOTHING, verbose_name='Produto'
    )
    quantidade = models.IntegerField('Quantidade', null=True)
    preco = models.DecimalField('Preço do Produto', max_digits=10, decimal_places=2, null=True, blank=True, default=5)
    subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, default=0)
    detalhes = models.CharField('Detalhes da Compra', max_length=300, blank=True) 

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def save(self, *args, **kwargs):
        self.subtotal = self.quantidade * self.preco
        return super(CompraProduto, self).save(*args, **kwargs)

    def precoProduto(self):
        return "R$ %s" % number_format(self.preco, 2)

    def subTotalProduto(self):
        return "R$ %s" % number_format(self.subtotal, 2)

    def __str__(self) -> str:
        return f'{self.compra.codigo}' 


@receiver(post_save, sender=CompraProduto)
def total(sender, instance, *args, **kwargs):
    order = Compra.objects.filter(id=instance.compra_id)
    for s in order:
        s.total += instance.subtotal
        s.save()


@receiver(post_delete, sender=CompraProduto)
def total(sender, instance, *args, **kwargs):
    order = Compra.objects.filter(id=instance.compra_id)
    for s in order:
        s.total -= instance.subtotal
        s.save()


class CompraPrestacao(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    prestacao = models.CharField('Parcela', max_length=5)
    valor = models.DecimalField('Valor da Parcela', max_digits=10, decimal_places=2, default=0)
    vencimento = models.DateField('Vencimento')
    pagamento = models.DateField('Pagamento')
    
    class Meta:
        verbose_name = 'Prestação'
        verbose_name_plural = 'Prestações'     


class Venda(models.Model):
    codigo = models.CharField('Código da Venda', max_length=10)
    data = models.DateField('Data da Venda')
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)    
    formapgto = models.CharField(
        'Forma de Pagamento', max_length=11, choices=PGTO_CHOICES)
    total = models.DecimalField('Total da Venda', max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    status = models.CharField('Condição', max_length=10, choices=STATUS_CHOICES, default='pendente')

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def totalVenda(self):
        return "R$ %s" % number_format(self.total, 2)     

    def __str__(self) -> str:
        return f'{self.cliente} - {self.data.day}/{self.data.month}/{self.data.year}'              


class VendaProduto(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, on_delete=models.DO_NOTHING, verbose_name='Produto'
    )
    quantidade = models.PositiveSmallIntegerField('Quantidade', default=0)
    preco = models.DecimalField('Valor Produto', max_digits=10, decimal_places=2, null=True, blank=True, default=5)
    subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, default=0)
    detalhes = models.CharField('Detalhes da Venda', max_length=300, blank=True)   

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def save(self, *args, **kwargs):
        self.subtotal = self.quantidade * self.preco
        return super(VendaProduto, self).save(*args, **kwargs)

    def precoProduto(self):
        return "R$ %s" % number_format(self.preco, 2)

    def subTotalProduto(self):
        return "R$ %s" % number_format(self.subtotal, 2)

    def __str__(self) -> str:
        return f'{self.venda.codigo}' 


@receiver(post_save, sender=VendaProduto)
def total(sender, instance, *args, **kwargs):
    order = Venda.objects.filter(id=instance.venda_id)
    for s in order:
        s.total += instance.subtotal
        s.save()


@receiver(post_delete, sender=VendaProduto)
def total(sender, instance, *args, **kwargs):
    order = Venda.objects.filter(id=instance.venda_id)
    for s in order:
        s.total -= instance.subtotal
        s.save()


class VendaPrestacao(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    prestacao = models.CharField('Parcela', max_length=5)
    valor = models.DecimalField('Valor da Parcela', max_digits=10, decimal_places=2, default=0)
    vencimento = models.DateField('Vencimento')
    pagamento = models.DateField('Pagamento')
    
    class Meta:
        verbose_name = 'Prestação'
        verbose_name_plural = 'Prestações'