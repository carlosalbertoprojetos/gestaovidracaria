from wsgiref.validate import validator
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

    #calculo valor icms 1    
    def icms_interno_1(self):
        self.icms_1 = self.aliquota_1 * self.valor_venda_produto()         
        return round(self.icms_1,2)
    
    #calculo valor ipi
    def calculo_ipi(self):
        self.valor_ipi = self.valor_venda_produto() * self.ipi 
        return round(self.valor_ipi, 2) 
    
    #calculo do frete    
    def calculo_frete(self):        
        self.frete = (self.valor_venda_produto() * self.taxa_frete) + self.valor_frete 
        return round(self.frete, 2)

    #Base calculo ST =(J5+V5+S5)*(1+(W5/100))
    def base_calculo_st(self):       
        self.st = float((self.valor_venda_produto() + self.calculo_frete() + self.calculo_ipi())) * (1 + int(self.mva)/100)
        return round(self.st, 2) 
    
    #Base de calculo do icms 2 e ST 
    def calculo_icms_st(self):
        self.icmsST = self.valor_venda_produto() + self.calculo_frete() 
        return round(self.icmsST, 2) 
    
    #calculo valor icms 2
    def icms_interno_2(self):
        self.icms_2 = self.aliquota_2 * self.calculo_icms_st() 
        return round(self.icms_2, 2)     

    #calculo ST =(X5*(K5)-O5)
    def calculo_st(self):
        self.st = ((float(self.aliquota_1)) * self.base_calculo_st()) - float(self.icms_interno_2()) 
        return round(self.st, 2)

    #calculo diferença de aliquota ICMS
    def diferenca_aliquota_icms(self):
        self.al_icms = (self.aliquota_1 - self.aliquota_2) * self.valor_venda_produto() 
        return round(self.al_icms, 2)
         
    #calculo custo final do produto =J5+Q5+Y5
    def calculo_preco_final(self):
        self.preco_final = float(self.valor_venda_produto()) + float(self.diferenca_aliquota_icms()) + float(self.calculo_st()) 
        return round(self.preco_final, 2)

    #calculo custo fracionado do produto
    def custo_fracionado_produto(self):
        if self.unimed.unidade == "KG":
            self.frac_produto = self.calculo_preco_final() / 6
        if self.unimed.unidade == "PÇ":
            self.frac_produto = self.calculo_preco_final()
        if self.unimed.unidade == "M2":
            self.frac_produto = self.calculo_preco_final()     
        
        return round(self.frac_produto, 2)    
    
    #calculo venda fracionada do produto
    def custo_venda_fracionada(self):
        self.venda_frac = self.custo_fracionado_produto() * 2 
        return round(self.venda_frac, 2)

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