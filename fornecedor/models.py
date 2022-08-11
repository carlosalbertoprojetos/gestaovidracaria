from django.db import models
from django_cpf_cnpj.fields import CNPJField, CPFField
from phonenumber_field.modelfields import PhoneNumberField

from banco.models import Banco
# Create your models here.

class Fornecedor(models.Model):

	STATE_CHOICES = (
		('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'),
		('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'),
		('MG','MG'), ('PA','PA'), ('PB','PB'), ('PE','PE'), ('PI','PI'), ('PR','PR'), 
		('RJ','RJ'), ('RN','RN'), ('RO','RO'), ('RR','RR'), ('RS','RS'), ('SC','SC'), 
		('SE','SE'), ('SP','SP'), ('TO','TO'),
    
    )

	nome_fornecedor = models.CharField('Nome Fornecedor',max_length=200)
	nome_contato = models.CharField('Nome Contato',max_length=200)
	banco = models.ForeignKey(Banco, on_delete=models.DO_NOTHING, verbose_name='Banco')
	tel_principal = models.CharField('Telefone Principal',max_length=11, unique = True, blank = True)
	tel_contato = models.CharField('Telefone Contato',max_length=11, unique = True, blank = True)
	email = models.EmailField('E-mail', max_length=254,unique=True, blank=True)	
	cnpj = models.CharField('CNPJ',max_length=18, unique = True, blank = True)
	insc_estadual = models.CharField('Inscrição Estadual',max_length=15, unique = True, blank=True)
	logradouro = models.CharField('Logradouro', max_length=200, blank=True)
	numero = models.CharField('Número', max_length=30, blank=True)
	complemento = models.CharField('Complemento', max_length=100, blank=True)
	cep = models.CharField('CEP', max_length=11, blank=True)
	estado = models.CharField('Estado', choices=STATE_CHOICES,max_length=2, blank=True)
	cidade = models.CharField('Cidade',max_length=100, null=True, blank=True)
	
	class Meta:
		ordering = ['nome_fornecedor', ]
		verbose_name = 'Fornecedor'
		verbose_name_plural = 'Fornecedores'
	
	def __str__(self):
		return self.nome_fornecedor