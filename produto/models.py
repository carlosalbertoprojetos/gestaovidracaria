from django.db import models
from django.db import connection
from django.urls import reverse
import locale
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from django.core.exceptions import ValidationError
from tourproject.constantes import TAXAS_CHOICES
from fornecedor.models import Fornecedor


 
def validate_campos(value):
    if not value.isdigit():
        raise ValidationError('O campo deve conter apenas números')


#==================================================================================================
#CATEGORIA

class Categoria(models.Model):
    nome = models.CharField('Categoria', max_length=255)
    descricao = models.TextField('Descrição', blank=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome

#==================================================================================================
#UNIDADE DE MEDIDA

class UnidadeMedida(models.Model):
    unidade = models.CharField('Un', max_length=10)
    descricao = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = "Unidade de Medida"
        verbose_name_plural = "Unidades de Medida"

    def __str__(self):
        return self.unidade

#==================================================================================================
#PRODUTO

class Produto(models.Model):
    nome = models.CharField('Produto', max_length=255)
    codigo = models.CharField('Código',max_length=10)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, verbose_name='Categoria')
    unimed = models.ForeignKey(UnidadeMedida, on_delete=models.DO_NOTHING, verbose_name='Unidade')
    ncm = models.CharField('NCM',max_length=10, validators=[validate_campos])
    cst = models.CharField('CST',max_length=3, validators=[validate_campos])
    cfop = models.CharField('CFOP',max_length=4, validators=[validate_campos])
    peso_barra = models.DecimalField('Peso Barra', max_digits=9, decimal_places=2,default=0.0)
    estoque_ini = models.DecimalField('Estoque Inicial', max_digits=10, decimal_places=2, default=0.0)
    descricao = models.TextField('Descrição', blank=True)
    status_disponivel = models.BooleanField('Disponível', default=True)
    criadoem = models.DateTimeField(auto_now_add=True)
    atualizadoem = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return str(self.nome)

#==================================================================================================
#TRIBUTOS

class Tributos(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor_unitario = models.DecimalField('Valor unitário R$', max_digits=9, decimal_places=2, default=0.0)
    valor_barra_un = models.DecimalField('Valor Barra/un R$', max_digits=9, decimal_places=2, default=0.0)
    taxa_icms_interno = models.DecimalField('ICMS INTERNO', max_digits=9, decimal_places=2, default=0.0)
    taxa_icms_inter = models.DecimalField('ICMS INTER', max_digits=9, decimal_places=2, default=0.0)
    icms_interno = models.DecimalField('ICMS INTERNO',max_digits=6, decimal_places=4, default=0.0)
    icms_inter = models.DecimalField('ICMS INTER', max_digits=9, decimal_places=2, default=0.0)
    ali_dif_icms = models.DecimalField('AL ICMS', max_digits=9, decimal_places=2, default=0.0)
    dif_aliq_icms = models.DecimalField('DIF AL ICMS', max_digits=9, decimal_places=2, default=0.0)
    taxa_ipi = models.DecimalField('IPI',  max_digits=9, decimal_places=2, default=0.0)
    ipi = models.DecimalField('IPI',  max_digits=9, decimal_places=2, default=0.0)
    taxa_frete = models.DecimalField('Taxa do Frete', max_digits=9, decimal_places=2, default=0.0)
    valor_frete = models.DecimalField('Frete R$', max_digits=9, decimal_places=2, default=0.0)
    frete = models.DecimalField('FRETE', max_digits=9, decimal_places=2, default=0.0)
    base_icms_st = models.DecimalField('BASE CALCULO ICMS INTER ST', max_digits=9, decimal_places=2, default=0.0)
    base_calc_st = models.DecimalField('BASE CALCULO ST', max_digits=9, decimal_places=2, default=0.0)
    st = models.DecimalField('ST', max_digits=9, decimal_places=2, default=0.0)
    custo_final = models.DecimalField('CUSTO FINAL DA BARRA', max_digits=9, decimal_places=2, default=0.0)
    custo_frac = models.DecimalField('CUSTO FRACIONADO - ml', max_digits=9, decimal_places=2, default=0.0)
    preco_frac = models.DecimalField('PREÇO DE VENDA fracionada -ml', max_digits=9, decimal_places=2, default=0.0)
    mva = models.DecimalField('MVA',max_digits=6, decimal_places=4, default=0.0)
    criadoem = models.DateTimeField(auto_now_add=True)
    atualizadoem = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tributo"
        verbose_name_plural = "Tributos"
        
    def save(self, *args, **kwargs):
        self.valor_barra_un = self.valor_unitario * Decimal(self.produto.peso_barra)
        self.icms_interno = self.valor_barra_un * Decimal(self.taxa_icms_interno)
        self.frete = (self.valor_barra_un * Decimal(self.taxa_frete)) + Decimal(self.valor_frete)
        self.base_icms_st = self.valor_barra_un + Decimal(self.frete)
        self.icms_inter = self.base_icms_st * Decimal(self.taxa_icms_inter)
        self.ali_dif_icms = self.taxa_icms_interno - self.taxa_icms_inter
        self.dif_aliq_icms = self.valor_barra_un *  self.ali_dif_icms
        self.ipi = self.valor_barra_un * Decimal(self.taxa_ipi)
        self.base_calc_st = Decimal(self.valor_barra_un + self.ipi + self.frete)
        self.st = (self.base_calc_st * Decimal(self.taxa_icms_interno)) - self.icms_inter
        self.custo_final = self.valor_barra_un + Decimal(self.dif_aliq_icms) + Decimal(self.st)
        self.custo_frac = Decimal(self.custo_final)/6
        self.preco_frac = Decimal(self.custo_frac) * 2
        return super(Tributos, self).save(*args, **kwargs)

    def __str__(self):
        return '{0} - criado em {1}'.format(str(self.produto), self.criadoem)


#==================================================================================================
#CALCULOS

# class Calculos(models.Model):
#     produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
#     tributos = models.ForeignKey(Tributos, on_delete=models.DO_NOTHING, verbose_name='Produto')
#     valor_barra_un = models.DecimalField('Valor Barra/un R$', default=0.0)
#     icms_interno = models.DecimalField('ICMS INTERNO',max_digits=6, decimal_places=4, default=0.0)
#     base_icms_st = models.DecimalField('BASE CALCULO ICMS INTER ST', max_digits=9, decimal_places=2, default=0.0)
#     icms_inter = models.DecimalField('ICMS INTER', max_digits=9, decimal_places=2, default=0.0)
#     ali_dif_icms = models.DecimalField('AL ICMS', max_digits=9, decimal_places=2, default=0.0)
#     dif_aliq_icms = models.DecimalField('DIF AL ICMS', max_digits=9, decimal_places=2, default=0.0)
#     ipi = models.DecimalField('IPI',  max_digits=9, decimal_places=2, default=0.0)
#     frete = models.DecimalField('FRETE', max_digits=9, decimal_places=2, default=0.0)
#     base_calc_st = models.DecimalField('BASE CALCULO ST', max_digits=9, decimal_places=2, default=0.0)
#     st = models.DecimalField('ST', max_digits=9, decimal_places=2, default=0.0)
#     custo_final = models.DecimalField('CUSTO FINAL DA BARRA', max_digits=9, decimal_places=2, default=0.0)
#     custo_frac = models.DecimalField('CUSTO FRACIONADO - ml', max_digits=9, decimal_places=2, default=0.0)
#     preco_frac = models.DecimalField('PREÇO DE VENDA fracionada -ml', max_digits=9, decimal_places=2, default=0.0)
#     criadoem = models.DateTimeField(auto_now_add=True)
#     atualizadoem = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = "Calculo"
#         verbose_name_plural = "Calculos"

#     def __str__(self):
#         return f'{self.tributos.produto}'
