#from email.policy import default
#from email.utils import formatdate
#from statistics import quantiles
from django.db import models
#from django.db.models.signals import post_save
#from django.dispatch import receiver
from django.utils.formats import number_format
from gestaovidracaria.constantes import STATUS_CHOICES, PGTO_CHOICES

from produto.models import Produto
from cliente.models import Cliente
from fornecedor.models import Fornecedor

class Compra(models.Model):
    codigo_compra = models.CharField('Código Compra', max_length=10)
    data_compra = models.DateField('Data Compra')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    formapgto_compra = models.CharField('Forma pgto', max_length=11, choices=PGTO_CHOICES)
    imagem_compra = models.ImageField(upload_to='nfs_compras', blank=True, null=True)
    total_compra = models.DecimalField('Custo da Compra R$', max_digits=11, decimal_places=2, null=True, blank=True, default=0)
    status = models.CharField('Condição', max_length=10, choices=STATUS_CHOICES, default='pendente')

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self) -> str:
        return f'{self.data_compra.day}/{self.data_compra.month}/{self.data_compra.year}'  

class CompraProduto(models.Model):

    compra_produto = models.ForeignKey(Compra, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, on_delete=models.DO_NOTHING, verbose_name='Produto'
    )
    quant_produto_compra = models.IntegerField('Quantidade', null=True)
    preco_compra_produto = models.DecimalField('Preço de Compra R$', max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    subtotal = models.DecimalField('Subtotal R$', max_digits=10, decimal_places=2, default=0)
    detalhes_compra = models.CharField('Detalhes da Compra', max_length=300, blank=True) 

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self) -> str:
        return f'{self.compra_produto.fornecedor}'       

class Venda(models.Model):
    codigo_venda = models.CharField('Código da Venda', max_length=10)
    data_venda = models.DateField('Data Venda')
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)    
    #num_venda = models.CharField('Código da Venda', max_length=10)
    formapgto_venda = models.CharField(
        'Forma pgto', max_length=11, choices=PGTO_CHOICES)
    custo_venda = models.DecimalField('Custo da venda R$', max_digits=10, decimal_places=2,null=True, blank=True, default=0)
    #total_venda = models.DecimalField(
    #    'Total', max_digits=11, decimal_places=2, null=True, blank=True, default=0)
    status = models.CharField('Condição', max_length=10, choices=STATUS_CHOICES, default='pendente')

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def custovenda(self):
        self.codigo_venda.custo_venda = 10.00 
        return "R$ %s" % number_format(self.codigo_venda.custo_venda, 2)     

    def __str__(self) -> str:
        return f'{self.cliente} - {self.data_venda.day}/{self.data_venda.month}/{self.data_venda.year}'              

'''
@receiver(post_save, sender=Venda)
def estoque_venda(sender, instance, **kwargs):    
    produto = Produto.objects.filter(pk=instance.produto_id)

    for p in produto:
        p.estoque -= instance.quantidade
        p.save()
        instance.venda.total += instance.subtotal
        instance.venda.save()
'''
class VendaProduto(models.Model):

    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, on_delete=models.DO_NOTHING, verbose_name='Produto'
    )
    quant_produto_venda = models.PositiveSmallIntegerField('Quantidade', default=0)
    preco_venda_produto = models.DecimalField('Preço de Venda R$', max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    detalhes_venda = models.CharField('Detalhes da Venda', max_length=300, blank=True)
    
    #remover esse campo
    #subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        
    def subtotal(self):
        self.sub_total = self.produto.valor * self.quant_produto_venda
        return "R$ %s" % number_format(self.sub_total, 2)

    def save(self, *args, **kwargs):
        self.subtotal = self.produto.valor * self.quant_produto_venda
        # print(self.subtotal)
        super(VendaProduto, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.venda.codigo_venda}' 
    


# class Compra(models.Model):
#     data = models.DateField('Data')
#     fornecedor = models.ForeignKey(
#         Fornecedor, on_delete=models.DO_NOTHING)
#     formapgto = models.CharField(
#         'Forma pgto', max_length=11, choices=PGTO_CHOICES)
#     imagem = models.ImageField(upload_to='nfs_compras', blank=True, null=True)
#     total = models.DecimalField(
#         'Total', max_digits=11, decimal_places=2, null=True, blank=True, default=0)
#     status = models.CharField(
#         'Condição da entrega', max_length=10, choices=STATUS_CHOICES, default='pendente')
#     pgto_avista = models.DecimalField(
#         'Valor a vista', max_digits=11, decimal_places=2, null=True, blank=True, default=0)

#     class Meta:
#         verbose_name = 'Compra'
#         verbose_name_plural = 'Compras'


# class CompraProduto(models.Model):
#     compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
#     produto = models.ForeignKey(
#         Produto, on_delete=models.DO_NOTHING, verbose_name='Produto'
#     )
#     quantidade = models.IntegerField('Quantidade', null=True)
#     preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
#     subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, default=0)
#     detalhes = models.CharField('Detalhes', max_length=300, blank=True)
    

class CompraPrestacao(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    prestacao = models.CharField('Parcela', max_length=5)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0)
    vencimento = models.DateField('Vencimento')
    pagamento = models.DateField('Pagamento')
    
    class Meta:
        verbose_name = 'Prestação'
        verbose_name_plural = 'Prestações'
    

# class Venda(models.Model):
#     data = models.DateField('Data')
#     cliente = models.ForeignKey(
#         Cliente, on_delete=models.DO_NOTHING)
#     num_venda = models.IntegerField('Nº Venda')
#     formapgto = models.CharField(
#         'Forma pgto', max_length=11, choices=PGTO_CHOICES)
#     custo = models.DecimalField('Custo da venda', max_digits=10, decimal_places=2)
#     imagem = models.ImageField(upload_to='nfs_compras', blank=True, null=True)
#     total = models.DecimalField(
#         'Total', max_digits=11, decimal_places=2, null=True, blank=True, default=0)
#     status = models.CharField(
#         'Condição da entrega', max_length=10, choices=STATUS_CHOICES, 
#         default='pendente')
#     pgto_avista = models.DecimalField(
#         'Valor a vista', max_digits=11, decimal_places=2, null=True, blank=True, default=0)

#     class Meta:
#         verbose_name = 'Venda'
#         verbose_name_plural = 'Vendas'


# @receiver(post_save, sender=Venda)
# def estoque_venda(sender, instance, **kwargs):    
#     produto = Produto.objects.filter(pk=instance.produto_id)

#     for p in produto:
#         p.estoque -= instance.quantidade
#         p.save()
#         instance.venda.total += instance.subtotal
#         instance.venda.save()


# class VendaProduto(models.Model):
#     venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
#     produto = models.ForeignKey(
#         Produto, on_delete=models.DO_NOTHING, verbose_name='Produto'
#     )
#     quantidade = models.IntegerField('Quantidade', null=True)
#     preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
#     detalhes = models.CharField('Detalhes', max_length=300, blank=True)
#     subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, default=0)
    

class VendaPrestacao(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    prestacao = models.CharField('Parcela', max_length=5)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0)
    vencimento = models.DateField('Vencimento')
    pagamento = models.DateField('Pagamento')
    
    class Meta:
        verbose_name = 'Prestação'
        verbose_name_plural = 'Prestações'