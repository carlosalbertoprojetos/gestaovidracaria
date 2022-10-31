from ast import Break
import pdb
from pyexpat import model
from django.db import models
from django.urls import reverse
from django.utils.formats import number_format
from django.core.exceptions import ValidationError
from fornecedor.models import Fornecedor
from produto.models import Produto
from financeiro.models import Venda, Compra, VendaProduto, CompraProduto

class Fisico(models.Model):
    
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING, verbose_name='Produto')
    data_modificacao = models.DateField('Data de modificação', auto_now=True)    

    class Meta:        
        verbose_name = " Estoque Físico"        

    def codigo_produto(self):        
        return self.produto.codigo

    def estoque_inicial(self):
        return self.produto.quantidade        
    
    def nome_produto(self):
        return self.produto.nome

    def unidade_medida(self):                
        return self.produto.unimed

    def estoque_atual(self):
        #corrigir o filtro de pesquisa por produto e forncedor
        #pdb.set_trace()
        #for f in Fornecedor.objects.all():
        #    print(f)
        
        p = Produto.objects.count()
        #id = Produto.objects.filter()
        #qs = Produto.objects.filter(Venda=self.pk).values_list('codigo', 'quantidade') or 0
        #print(qs)    
        #p = Produto.objects.filter(id = self.fornecedor.pk)
        #print(p)
        
        if self.produto.unimed.unidade == 'KG' or 'ML':
                   
            self.valor_atual = float(self.produto.peso_barra/6 + self.produto.quantidade) - 2.5# - VendaProduto.quantidade
           # print('Quanti kg',self.produto.quantidade)
           # print(self.valor_atual)                
           
        
        if self.produto.unimed.unidade == "PÇ" or "M2":
            #print('quant pç',self.produto.quantidade)
            self.valor_atual = self.produto.quantidade + 9 #+ self.CompraProduto.quantidade# - VendaProduto.quantidade
        
        return round(self.valor_atual,2)

    def custo_fracionado(self):
        return self.produto.custo_fracionado_produto()

    def valor_total_custo(self):
        self.val_total_custo = self.custo_fracionado() * float(self.estoque_atual() or 0)
        return round(self.val_total_custo,2) 

    def __str__(self):
        return self.fornecedor.nome

class Fiscal(models.Model):
    
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING, verbose_name='Produto')
    data_modificacao = models.DateField('Data de modificação', auto_now=True)    

    class Meta:        
        verbose_name = "Estoque Fiscal"
        
    def codigo(self):
        return self.produto.codigo

    def estoque_inicial(self):
        return self.produto.quantidade        
    
    def nome_produto(self):
        return self.produto.nome

    def unidade(self):
        return self.produto.unimed.unidade

    def estoque_atual(self):
        #print(self.produto.unimed.unidade)
        if self.produto.unimed.unidade == "ML" or "KG":
            self.estoqueAtual = (self.produto.quantidade + (self.produto.peso_barra / 6)) - VendaProduto.quantidade        
        if self.produto.unimed.unidade == "PÇ" or "M2":
            
            self.estoqueAtual = (self.produto.quantidade + CompraProduto.quantidade) - VendaProduto.quantidade
              
        return round(self.estoqueAtual,2)           
    
    def custo_fracionado(self):
        return self.produto.custo_fracionado_produto() 

    def valor_total_custo(self):
        self.val_total_custo = self.produto.custo_fracionado_produto() * self.estoque_atual() or 0 

    def nome(self):
        return self.produto.nome
    
    def __str__(self):
        return self.fornecedor.nome