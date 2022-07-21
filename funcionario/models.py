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
	data_admissao = models.DateTimeField('Data Admissão')
	banco = models.ForeignKey(Banco, on_delete=models.DO_NOTHING, verbose_name='Banco')
	cargo = models.CharField('Cargo',max_length=200)
	salario = models.CharField('Salário',max_length=200)
	data_nascimento = models.DateTimeField('Data de Nascimento')
	naturalidade = models.CharField('Local de nascimento/UF', max_length=200)
	vale_transporte = models.TextField('Vale Transporte', blank=True)
	tel_residencial = PhoneNumberField('Telefone Residencial',unique = True, null = False, blank = False)
	tel_celular = PhoneNumberField('Telefone Celular',unique = True, null = False, blank = False)
	escolaridade = models.CharField('Escolaridade', max_length=200)
	estado_civil = models.CharField('Estado Civil',max_length=50)
	sexo = models.CharField('Sexo', choices=SEXO_CHOICES, max_length=18)
	raca_cor = models.CharField('Raça/Cor', choices=RACA_CHOICES,max_length=8)
	email = models.EmailField('E-mail', max_length=254,unique=True)
	rg = models.CharField('RG', max_length=7)
	data_rg = models.DateTimeField('Data Expedição')
	cpf = CPFField(masked=True)
	ctps = models.CharField('CTPS/SÉRIE/UF', max_length=50)		
	pis = models.CharField('PIS', max_length=15)
	titulo_eleitor = models.CharField('TITULO/SEÇÃO/ZONA/UF', max_length=200)
	cnh = models.CharField('CNH', max_length=50)
	logradouro = models.CharField('Logradouro', max_length=200)
	numero = models.CharField('Número', max_length=30)
	complemento = models.CharField('Complemento', max_length=100, null=True)
	cep = models.CharField('CEP', max_length=11)
	estado = models.CharField('Estado', choices=STATE_CHOICES, max_length=2)
	cidade = models.CharField('Cidade',max_length=100, null=True)
	nome_pai = models.CharField('Nome do Pai', max_length=200)
	nome_mae = models.CharField('Nome da Mãe', max_length=200)
	nome_conjuge = models.CharField('Nome do Cônjuge', max_length=200)
	nome_filho = models.CharField('Nome do Filho', max_length=200)
	data_nasc_filho = models.DateTimeField('Data de Nascimento do Filho')


	def __str__(self):
		return self.nome_funcionario
