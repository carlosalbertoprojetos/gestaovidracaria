from django.db import models
from django.core.validators import RegexValidator


STATE_CHOICES = (
		('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'),
		('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'),
		('MG','MG'), ('PA','PA'), ('PB','PB'), ('PE','PE'), ('PI','PI'), ('PR','PR'), 
		('RJ','RJ'), ('RN','RN'), ('RO','RO'), ('RR','RR'), ('RS','RS'), ('SC','SC'), 
		('SE','SE'), ('SP','SP'), ('TO','TO'),
    
    )

class Banco(models.Model):	
	
	nome = models.CharField('Banco/Refência',max_length=30,)
	agencia = models.CharField('Agência',max_length=30)
	conta = models.CharField('Conta',max_length=30)	
	saldo_dia = models.DecimalField('Saldo Inicial R$', max_digits=9, decimal_places=3, default=0.00,blank=True)	
	pix = models.CharField('Chave PIX',max_length=30, blank=True)	
	tel_contato = models.CharField('Telefone Contato',max_length=11, unique = True,blank =True)	
	logradouro = models.CharField('Logradouro', max_length=200, blank=True,)	
	numero = models.CharField('Número', max_length=5, blank=True)
	complemento = models.CharField('Complemento', max_length=100, blank=True)	
	cep = models.CharField('CEP', max_length=11, blank=True)	
	estado = models.CharField('Estado', choices=STATE_CHOICES,  max_length=2, blank=True)	
	cidade = models.CharField('Cidade',max_length=100, blank=True)

	def __str__(self):
		return self.nome


class CaixaDia(models.Model):
	nome = models.CharField('Banco/Refência',max_length=30,
	validators=[RegexValidator('([A-Z])\w+',
								'Somente letras maiúsculas.')],)
	agencia = models.CharField('Agência',max_length=30)
	conta = models.CharField('Conta',max_length=30)
	saldo_dia = models.DecimalField('Saldo Inicial R$', max_digits=9, decimal_places=3, blank=True, null=True)

	pix = models.CharField('Chave PIX',max_length=30, blank=True)	
	tel_contato = models.CharField('Telefone Contato',max_length=11, unique = True,blank =True )
	logradouro = models.CharField('Logradouro', max_length=200, blank=True,
	validators=[RegexValidator('([A-Z])\w+',
								'Somente letras maiúsculas.')],)	
	numero = models.CharField('Número', max_length=5, blank=True)
	complemento = models.CharField('Complemento', max_length=100, blank=True)
	cep = models.CharField('CEP', max_length=11, blank=True)
	estado = models.CharField('Estado', choices=STATE_CHOICES,  max_length=2, blank=True)
	cidade = models.CharField('Cidade',max_length=100, blank=True)	

	class Meta:
		verbose_name = 'Caixa'
		verbose_name_plural = 'Caixa'

	def __str__(self):
		return f'{self.nome}'