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
        ordering = ["fornecedor"]
        verbose_name = "Físico"
        

    def codigo(self):
        return self.produto.codigo

    def estoque_inicial(self):
        return self.produto.quantidade        
    
    def nome_produto(self):
        return self.produto.nome

    def unidade(self):
        return self.produto.unimed

    def estoque_atual(self):
        if self.produto.unimed == "ML":
            self.estoqueAtual = (self.produto.quantidade + (self.produto.peso_barra / 6)) - VendaProduto.quantidade        
        if self.produto.unimed == "PÇ" or "M2":
            self.estoqueAtual = (self.produto.quantidade + CompraProduto.quantidade) - VendaProduto.quantidade
              
        return round(self.estoqueAtual,2)           
    
    def custo_fracionado(self):
        return self.produto.custo_fracionado_produto()

    def valor_total_custo(self):
        self.val_total_custo = self.produto.custo_fracionado_produto() * self.estoque_atual() 

    def __str__(self):
        return self.fornecedor

class Fiscal(models.Model):
    
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING, verbose_name='Produto')
    data_modificacao = models.DateField('Data de modificação', auto_now=True)    

    class Meta:
        ordering = ["fornecedor"]
        verbose_name = "Fiscal"
        

    def codigo(self):
        return self.produto.codigo

    def estoque_inicial(self):
        return self.produto.quantidade        
    
    def nome_produto(self):
        return self.produto.nome

    def unidade(self):
        return self.produto.unimed

    def estoque_atual(self):
        if self.produto.unimed == "ML":
            self.estoqueAtual = (self.produto.quantidade + (self.produto.peso_barra / 6)) - VendaProduto.quantidade        
        if self.produto.unimed == "PÇ" or "M2":
            self.estoqueAtual = (self.produto.quantidade + CompraProduto.quantidade) - VendaProduto.quantidade
              
        return round(self.estoqueAtual,2)           
    
    def custo_fracionado(self):
        return self.produto.custo_fracionado_produto()

    def valor_total_custo(self):
        self.val_total_custo = self.produto.custo_fracionado_produto() * self.estoque_atual() 

    def __str__(self):
        return self.fornecedor