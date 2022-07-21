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
	tel_principal = PhoneNumberField('Telefone Principal',unique = True, null = False, blank = False)
	tel_contato = PhoneNumberField('Telefone Contato',unique = True, null = False, blank = False)
	email = models.EmailField('E-mail', max_length=254,unique=True)	
	cnpj = CNPJField(masked=True)
	insc_estadual = models.CharField('Inscrição Estadual',max_length=15, unique = True, null = False, blank = False)
	logradouro = models.CharField('Logradouro', max_length=200)
	numero = models.CharField('Número', max_length=30)
	complemento = models.CharField('Complemento', max_length=100, null=True)
	cep = models.CharField('CEP', max_length=11)
	estado = models.CharField('Estado', choices=STATE_CHOICES,  max_length=2)
	cidade = models.CharField('Cidade',max_length=100, null=True)
	
	
	def __str__(self):
		return self.nome_fornecedor