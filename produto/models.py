from ast import Mult
from audioop import mul
import pdb
from typing_extensions import Self
from django.db import models
from django.urls import reverse
from django.utils.formats import number_format
from django.core.exceptions import ValidationError
from fornecedor.models import Fornecedor


class Categoria(models.Model):
    nome = models.CharField('Categoria', max_length=255, unique=True)
    descricao = models.TextField('Descrição', blank=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class UnidadeMedida(models.Model):
    unidade = models.CharField('Un', max_length=10)   
    
    class Meta:
        verbose_name = "Unidade de Medida"
        verbose_name_plural = "Unidades de Medida"

    def __str__(self):
        return self.unidade    

def validate_campos(value):
    if not value.isdigit():
        raise ValidationError('O campo deve conter apenas números')

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    codigo = models.CharField('Código',max_length=10)
    nome = models.CharField('Produto', max_length=255, unique=True)
    ncm = models.CharField('NCM',max_length=10, validators=[validate_campos], blank=True)
    cst = models.CharField('CST',max_length=3, validators=[validate_campos],blank=True)
    cfop = models.CharField('CFOP',max_length=4, validators=[validate_campos], blank=True)
    peso_barra = models.DecimalField('Peso Barra', max_digits=4, decimal_places=2, default=0, blank=True)
    aliquota_1 = models.DecimalField('Aliquota Interno 1', max_digits=3, decimal_places=2, default=0.00, blank=True)
    aliquota_2 = models.DecimalField('Aliquota Interno 2', max_digits=3, decimal_places=2, default=0.00, blank=True)
    ipi = models.DecimalField('IPI', max_digits=3, decimal_places=2, default=0, blank=True)
    mva = models.CharField('MVA',max_length=3, validators=[validate_campos],blank=True)
    imagem = models.ImageField(
        'Imagem do produto', upload_to="produto/imagens/%Y", blank=True)
    unimed = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE, verbose_name='Unidade de medida')
    descricao = models.TextField('Descrição', blank=True)
    valor_custo = models.DecimalField('Valor de Custo R$', max_digits=10, decimal_places=2, default=0, blank=True)
    valor_venda = models.DecimalField('valor de Venda R$', max_digits=10, decimal_places=2, default=0, blank=True)
    status = models.BooleanField('Disponível', default=True)
    quantidade = models.DecimalField('Quantidade de Produto', max_digits=4, decimal_places=2, default=0, blank=True)
    taxa_frete = models.DecimalField('Taxa Frete', max_digits=5, decimal_places=4, default=0, blank=True)
    valor_frete = models.DecimalField('valor para frete R$', max_digits=4, decimal_places=2, default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    
    #calculo valor do produto
    def valor_venda_produto(self):       
        if self.unimed.unidade == 'KG':
            self.valor_produto = self.peso_barra * self.valor_venda
        if self.unimed.unidade == 'PÇ':
            self.valor_produto = self.valor_venda
        if self.unimed.unidade == 'M2':
            self.valor_produto = self.valor_venda
        if self.unimed.unidade == 'KIT':
            self.valor_produto = self.valor_venda

        return round(self.valor_produto,2)    
   
    v_produto = property(
        fget= valor_venda_produto
    )
    
    #calculo valor icms 1    
    def icms_interno_1(self):                        
        return round(self.aliquota_1 * self.v_produto,2)    
    
    #calculo valor ipi
    def calculo_ipi(self):
                    
        return round(self.v_produto * self.ipi , 2) 
    
    v_ipi = property(
        fget= calculo_ipi
    )
    
    #calculo do frete    
    def calculo_frete(self):      
        return round((self.v_produto * self.taxa_frete) + self.valor_frete , 2)
    
    v_frete = property(
        fget= calculo_frete
    )
    
    #Base calculo ST =(J5+V5+S5)*(1+(W5/100))
    def base_calculo_st(self):
        p = Produto.objects.filter(id=self.pk).values('pk').distinct() or 0
        print('Resposta->',p)            
        return round(float(self.v_produto + self.v_frete + self.v_ipi) * (1 + int(self.mva)/100), 2) 
    
    v_base_st = property(
        fget= base_calculo_st
    )
    
    #Base de calculo do icms 2 e ST 
    def calculo_icms_st(self):   
        return round(self.v_produto + self.v_frete, 2) 
    
    v_icms_st = property(
        fget= calculo_icms_st
    )
    
    #calculo valor icms 2
    def icms_interno_2(self):      
        return round(self.aliquota_2 * self.v_icms_st, 2)     

    v_icms_2 = property(
        fget= icms_interno_2
    )

    #calculo ST =(X5*(K5)-O5)
    def calculo_st(self):        
        return round(float(self.aliquota_1) * float(self.v_base_st) - float(self.v_icms_2), 2)

    v_st = property(
        fget= calculo_st
    )

    #calculo diferença de aliquota ICMS
    def diferenca_aliquota_icms(self):        
        return round(float(self.aliquota_1 - self.aliquota_2) * float(self.v_produto), 2)
         
    v_dif_aliquota_icms = property(
        fget= diferenca_aliquota_icms
    )
    
    #calculo custo final do produto =J5+Q5+Y5
    def calculo_preco_final(self):         
        return round(float(self.v_produto) + float(self.v_dif_aliquota_icms) + float(self.v_st), 2)

    #calculo custo fracionado do produto
    def custo_fracionado_produto(self):
        if self.unimed.unidade == "KG":
            self.frac_produto = self.calculo_preco_final() / 6
        if self.unimed.unidade == "PÇ":
            self.frac_produto = self.calculo_preco_final()
        if self.unimed.unidade == "M2":
            self.frac_produto = self.calculo_preco_final()     
        
        return round(self.frac_produto, 2)    
    
    v_custo_fracionado_produto = property(
        fget= custo_fracionado_produto
    )
    
    #calculo venda fracionada do produto
    def custo_venda_fracionada(self):         
        return round(self.v_custo_fracionado_produto * 2, 2)

    def get_absolute_url_Detail(self):
        return reverse('product:product_detail', args=[self.pk])
    
    def get_absolute_url_Update(self):
        return reverse('product:product_update', args=[self.pk])
    
    def get_absolute_url_Delete(self):
        return reverse('product:product_delete', args=[self.pk])
    
    def __str__(self):
        return self.nome

    #Calculo do frete

# @receiver(post_save, sender=Produto)
# def inventory_delete(sender, instance, **kwargs):
#     produto = Produto.objects.filter(pk=instance.produto_id)
#     for p in produto:
#         p.estoque -= instance.quantidade
#         p.save()

#     movimento = Movimento.objects.filter(pk=instance.movimento_id)
#     for o in movimento:
#         print('ORDER', o)
#     # order.total = sum
#     # order.save()

# @receiver(post_delete, sender=Produto)
# def inventory_insert(sender, instance, **kwargs):
#     produto = Produto.objects.filter(pk=instance.produto_id)
#     for p in produto:
#         p.estoque += instance.quantidade
#         p.save()