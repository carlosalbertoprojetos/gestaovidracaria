from django.db import models
# from django_cpf_cnpj.fields import CNPJField, CPFField
# from phonenumber_field.modelfields import PhoneNumberField
from gestaovidracaria.constantes import STATE_CHOICES

from conta.models import Conta
# Create your models here.

class Fornecedor(models.Model):
	nome = models.CharField('Fornecedor',max_length=200)
	contato = models.CharField('Nome do Contato',max_length=200)
	conta = models.ForeignKey(Conta, on_delete=models.DO_NOTHING, verbose_name='Banco')
	# tel_principal = PhoneNumberField('Telefone Principal',unique = True, blank=True)
	# tel_contato = PhoneNumberField('Telefone Contato',unique = True, blank=True)
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
		ordering = ['nome', ]
		verbose_name = 'Fornecedor'
		verbose_name_plural = 'Fornecedores'
	
	def __str__(self):
		return self.nome


class HistoricoFornecedor(models.Model):
        
    descricao = models.CharField(max_length=50)

    class Meta:
        ordering = ('descricao',)

    def __unicode__(self):
        return self.descricao