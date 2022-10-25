from django.db import models
from django.utils.formats import number_format
from gestaovidracaria.constantes import STATUS_CHOICES, PGTO_CHOICES

from produto.models import Produto
from cliente.models import Cliente
from fornecedor.models import Fornecedor
from conta.models import Conta

class Compra(models.Model):

    codigo = models.CharField('Código da Compra', max_length=10)
    data_compra = models.DateField('Data da compra')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    formapgto = models.CharField('Forma pgto', max_length=11, choices=PGTO_CHOICES)
    imagem = models.ImageField(upload_to='nfs_compras', blank=True, null=True)
    total = models.DecimalField('Custo da Compra R$', max_digits=11, decimal_places=2, null=True, blank=True, default=0)
    status = models.CharField('Condição', max_length=10, choices=STATUS_CHOICES, default='pendente')

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self) -> str:
        return f'{self.data_compra.day}/{self.data_compra.month}/{self.data_compra.year}'  

class CompraProduto(models.Model):

    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, on_delete=models.DO_NOTHING, verbose_name='Produto'
    )
    quantidade = models.IntegerField('Quantidade', null=True)
    preco = models.DecimalField('Valor da Compra R$', max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    subtotal = models.DecimalField('Subtotal R$', max_digits=10, decimal_places=2, default=0)
    detalhes = models.CharField('Detalhes da Compra', max_length=300, blank=True) 

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self) -> str:
        return f'{self.compra.codigo}'       

class Venda(models.Model):
    codigo = models.CharField('Código da Venda', max_length=10)
    data_venda = models.DateField('Data da Venda')
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    #conta = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)    
    formapgto = models.CharField(
        'Forma pgto', max_length=11, choices=PGTO_CHOICES)
    #num_parcelas = models.PositiveSmallIntegerField('Número de Parcelas',default=0)
    #data_venc = models.DateField('Data de Vencimento')
    #data_pgto = models.DateField('Data de Pagamento')
    custo = models.DecimalField('Custo da venda R$', max_digits=10, decimal_places=2,null=True, blank=True, default=0)
    status = models.CharField('Condição', max_length=10, choices=STATUS_CHOICES, default='pendente')

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    #def custovenda(self):
    #    self.codigo_venda.custo_venda = 10.00 
    #    return "R$ %s" % number_format(self.codigo.custo, 2)            

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
    quantidade = models.PositiveSmallIntegerField('Quantidade', default=0)
    preco = models.DecimalField('Preço de Venda R$', max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    detalhes = models.CharField('Detalhes da Venda', max_length=300, blank=True)   

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        
    def subtotal(self):
        self.sub_total = self.produto.valor_venda * self.quantidade
        return "R$ %s" % number_format(self.sub_total, 2)

    # conta os itens em cada venda
    def get_itens(self):
        return self.vendas_det.count()

    def custo_venda(self):
        qs = self.vendas_det.filter(sale=self.pk).values_list(
            'custoprice_sale', 'quantidade') or 0
        soma = 0 if isinstance(qs, int) else sum(map(lambda q: q[0] * q[1], qs))
        return "R$ %s" % number_format(soma, 2) 
    
    
    def save(self, *args, **kwargs):
        self.subtotal = self.produto.valor_venda * self.quantidade
        # print(self.subtotal)
        super(VendaProduto, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.venda.codigo}'     

class CompraPrestacao(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    prestacao = models.CharField('Parcela', max_length=5)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0)
    vencimento = models.DateField('Vencimento')
    pagamento = models.DateField('Pagamento')
    
    class Meta:
        verbose_name = 'Prestação'
        verbose_name_plural = 'Prestações'

# @receiver(post_save, sender=Venda)
# def estoque_venda(sender, instance, **kwargs):    
#     produto = Produto.objects.filter(pk=instance.produto_id)

#     for p in produto:
#         p.estoque -= instance.quantidade
#         p.save()
#         instance.venda.total += instance.subtotal
#         instance.venda.save()

class VendaPrestacao(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    prestacao = models.CharField('Parcela', max_length=5)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0)
    vencimento = models.DateField('Vencimento')
    pagamento = models.DateField('Pagamento')
    
    class Meta:
        verbose_name = 'Prestação'
        verbose_name_plural = 'Prestações'