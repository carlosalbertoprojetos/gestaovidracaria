from django.db import models
#from django_cpf_cnpj.fields import CNPJField, CPFField
#from phonenumber_field.modelfields import PhoneNumberField
from gestaovidracaria.constantes import STATE_CHOICES

# Create your models here.

class Cliente(models.Model):
    data_venda = models.DateTimeField('Data da Venda', auto_now_add=True)
    nome_cliente = models.CharField('Nome Completo',max_length=200)
    nome_contato = models.CharField('Nome Contato',max_length=200)
    tel_principal = models.CharField('Telefone Principal',max_length=11, unique = True, blank = True)
    tel_contato = models.CharField('Telefone Contato',max_length=11, unique = True, blank = True)
    email = models.EmailField('E-mail', max_length=254,unique=True, blank=True)
    cpf = models.CharField('CPF', max_length=14,unique = True, blank = True)
    cnpj = models.CharField('CNPJ',max_length=18, unique = True, blank = True)
    #cpf = CPFField(masked=True)
    #cnpj = CNPJField(masked=True)
    insc_estadual = models.CharField('Inscrição Estadual',max_length=15, unique = True,blank = True)
    logradouro = models.CharField('Logradouro', max_length=200, blank=True)
    numero = models.CharField('Número', max_length=30,blank=True)
    complemento = models.CharField('Complemento', max_length=100, blank=True)
    cep = models.CharField('CEP', max_length=11,blank=True)
    estado = models.CharField('Estado', choices=STATE_CHOICES,  max_length=2, blank=True)
    cidade = models.CharField('Cidade',max_length=100,blank=True)

    def __str__(self):
        return self.nome_cliente

class Obra(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, verbose_name='Cliente')
	responsavel = models.CharField('Responsável da Obra', max_length=200)
	logradouro_obra = models.CharField('Logradouro', max_length=200, blank=True)
	numero_obra = models.CharField('Número', max_length=30, blank=True)
	complemento_obra = models.CharField('Complemento', max_length=100,blank=True)
	cep_obra = models.CharField('CEP', max_length=11, blank=True)
	estado_obra = models.CharField('Estado', choices=STATE_CHOICES,max_length=2, blank=True)
	cidade_obra = models.CharField('Cidade',max_length=100, blank=True)

	def __str__(self):
		return self.numero_obra

