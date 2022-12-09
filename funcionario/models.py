from django.db import models
from gestaovidracaria.constantes import STATE_CHOICES, SEXO_CHOICES, RACA_CHOICES
# Create your models here.

from conta.models import Conta

class Funcionario(models.Model):

	empresa = models.CharField('Nome da Empresa',max_length=200)
	nome = models.CharField('Nome Completo',max_length=200)	
	admissao = models.DateField('Data de Admissão')
	banco = models.ForeignKey(Conta, on_delete=models.DO_NOTHING, verbose_name='Banco')
	cargo = models.CharField('Cargo',max_length=200, blank=True)
	salario = models.CharField('Salário',max_length=200, blank=True)
	nascimento = models.DateField('Data de Nascimento')
	naturalidade = models.CharField('Local de nascimento/UF', max_length=200, blank=True)
	vtransporte = models.TextField('Vale Transporte', blank=True)
	residencial = models.CharField('Telefone Residencial',max_length=11, unique = True, blank=True)
	celular = models.CharField('Celular',max_length=11, unique = True, blank=True)
	escolaridade = models.CharField('Escolaridade', max_length=200, blank=True)
	est_civil = models.CharField('Estado Civil',max_length=50, blank=True)
	sexo = models.CharField('Sexo', choices=SEXO_CHOICES, max_length=18, blank=True)
	raca = models.CharField('Raça/Cor', choices=RACA_CHOICES,max_length=8, blank=True)
	email = models.EmailField('E-mail', max_length=254,unique=True, blank=True)
	rg = models.CharField('RG', max_length=7, blank=True)
	data_rg = models.DateField('Data de Expedição')	
	cpf = models.CharField('CPF', max_length=14,unique = True, blank = True)
	ctps = models.CharField('CTPS/SÉRIE/UF', max_length=50, blank=True)		
	pis = models.CharField('PIS', max_length=15, blank=True)
	titulo = models.CharField('TITULO/SEÇÃO/ZONA/UF', max_length=200, blank=True)
	cnh = models.CharField('CNH', max_length=50, blank=True)
	logradouro = models.CharField('Logradouro', max_length=200, blank=True)
	numero = models.CharField('Número', max_length=30, blank=True)
	complemento = models.CharField('Complemento', max_length=100, blank=True)
	cep = models.CharField('CEP', max_length=11, blank=True)
	estado = models.CharField('Estado', choices=STATE_CHOICES, max_length=2, blank=True)
	cidade = models.CharField('Cidade',max_length=100, blank=True)
	pai = models.CharField('Nome do Pai', max_length=200, blank=True)
	mae = models.CharField('Nome da Mãe', max_length=200, blank=True)
	conjuge = models.CharField('Nome do Cônjuge', max_length=20, blank=True)	

	def __str__(self):
		return self.nome

class Filho(models.Model):
	funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING, verbose_name='Funcionario')
	nome = models.CharField('Nome do Filho', max_length=200, blank=True)
	data = models.DateField('Data de Nascimento')
	
	def __str__(self):
		return self.nome