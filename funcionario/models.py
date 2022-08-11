from unittest.util import _MAX_LENGTH
from django.db import models
from django_cpf_cnpj.fields import CNPJField, CPFField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

from banco.models import Banco

class Funcionario(models.Model):

	STATE_CHOICES = (
		('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'),
		('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'),
		('MG','MG'), ('PA','PA'), ('PB','PB'), ('PE','PE'), ('PI','PI'), ('PR','PR'), 
		('RJ','RJ'), ('RN','RN'), ('RO','RO'), ('RR','RR'), ('RS','RS'), ('SC','SC'), 
		('SE','SE'), ('SP','SP'), ('TO','TO'),
		)

	SEXO_CHOICES = (
		('M','M'), ('F','F'), ('OUTRO','OUTRO'), ('PREFIRO NÃO DIZER','PREFIRO NÃO DIZER'),
	)
	
	RACA_CHOICES = (
    	('BRANCA','BRANCA'), ('PRETA','PRETA'), ('PARDA','PARDA'), ('AMARELA','AMARELA'), ('INDÍGENA','INDÍGENA'),
    )

	nome_empresa = models.CharField('Nome da Empresa',max_length=200)
	nome_funcionario = models.CharField('Nome Completo',max_length=200)	
	data_admissao = models.DateField('Data Admissão')
	
	banco = models.ForeignKey(Banco, on_delete=models.DO_NOTHING, verbose_name='Banco', blank=True)	
	cargo = models.CharField('Cargo',max_length=200, blank=True)
	salario = models.CharField('Salário',max_length=200, blank=True)
	data_nascimento = models.DateField('Data de Nascimento')
	naturalidade = models.CharField('Local de nascimento/UF', max_length=200, blank=True)
	vale_transporte = models.TextField('Vale Transporte', blank=True)
	tel_residencial = models.CharField('Telefone Residencial',max_length=11, unique = True, blank=True)
	tel_celular = models.CharField('Telefone Celular',max_length=11, unique = True, blank=True)
	escolaridade = models.CharField('Escolaridade', max_length=200, blank=True)
	estado_civil = models.CharField('Estado Civil',max_length=50, blank=True)
	sexo = models.CharField('Sexo', choices=SEXO_CHOICES, max_length=18, blank=True)
	raca_cor = models.CharField('Raça/Cor', choices=RACA_CHOICES,max_length=8, blank=True)
	email = models.EmailField('E-mail', max_length=254,unique=True, blank=True)
	rg = models.CharField('RG', max_length=7, blank=True)
	data_rg = models.DateField('Data Expedição')	
	cpf = models.CharField('CPF', max_length=14,unique = True, blank = True)
	#cpf = CPFField(masked=True)
	ctps = models.CharField('CTPS/SÉRIE/UF', max_length=50, blank=True)		
	pis = models.CharField('PIS', max_length=15, blank=True)
	titulo_eleitor = models.CharField('TITULO/SEÇÃO/ZONA/UF', max_length=200, blank=True)
	cnh = models.CharField('CNH', max_length=50, blank=True)
	logradouro = models.CharField('Logradouro', max_length=200, blank=True)
	numero = models.CharField('Número', max_length=30, blank=True)
	complemento = models.CharField('Complemento', max_length=100, blank=True)
	cep = models.CharField('CEP', max_length=11, blank=True)
	estado = models.CharField('Estado', choices=STATE_CHOICES, max_length=2, blank=True)
	cidade = models.CharField('Cidade',max_length=100, blank=True)
	nome_pai = models.CharField('Nome do Pai', max_length=200, blank=True)
	nome_mae = models.CharField('Nome da Mãe', max_length=200, blank=True)
	nome_conjuge = models.CharField('Nome do Cônjuge', max_length=20, blank=True)	

	def __str__(self):
		return self.nome_funcionario

class Filho(models.Model):
	funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING, verbose_name='Funcionario')
	nome_filho = models.CharField('Nome do Filho', max_length=200, blank=True)
	data_nasc_filho = models.DateField('Data de Nascimento do Filho')
	
	def __str__(self):
		return self.nome_filho