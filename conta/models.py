from django.db import models
from django.utils.formats import number_format

from gestaovidracaria.constantes import STATE_CHOICES



class Conta(models.Model):
	nome = models.CharField('Banco',max_length=30)
	agencia = models.CharField('Agência',max_length=30)
	conta = models.CharField('Nome da Conta',max_length=30)	
	saldo = models.DecimalField('Saldo', max_digits=9, decimal_places=2, default=0)	
	pix = models.CharField('Chave PIX',max_length=30, blank=True)	
	tel_contato = models.CharField('Telefone Contato',max_length=11, unique = True,blank =True )	
	logradouro = models.CharField('Logradouro', max_length=200, blank=True)	
	numero = models.CharField('Número', max_length=5, blank=True)
	complemento = models.CharField('Complemento', max_length=100, blank=True)	
	cep = models.CharField('CEP', max_length=11, blank=True)	
	estado = models.CharField('Estado', choices=STATE_CHOICES,  max_length=2, blank=True)	
	cidade = models.CharField('Cidade',max_length=100, blank=True)
 
	def __str__(self):
		return self.nome

	def format_saldo(self):
		return "R$ %s" % number_format(self.saldo, 2)
