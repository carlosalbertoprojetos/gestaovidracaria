from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Banco(models.Model):

	STATE_CHOICES = (
     ('AC','AC'), ('AL','AL'), ('AP','AP'), 
     ('AM','AM'), ('BA','BA'), ('CE','CE'),
     ('DF','DF'), ('ES','ES'), ('GO','GO'),
     ('MA','MA'), ('MT','MT'), ('MS','MS'),
     ('MG','MG'), ('PA','PA'), ('PB','PB'),
     ('PE','PE'), ('PI','PI'), ('PR','PR'),
     ('RJ','RJ'), ('RN','RN'), ('RO','RO'),
     ('RR','RR'), ('RS','RS'), ('SC','SC'),
     ('SE','SE'), ('SP','SP'), ('TO','TO'),
    )
 
	nome_banco = models.CharField('Banco',max_length=30)
	agencia = models.CharField('Agência',max_length=30)
	conta = models.CharField('Conta',max_length=30)	
	saldo = models.DecimalField('Saldo', max_digits=9, decimal_places=2)	
	pix = models.CharField('PIX',max_length=30, blank=True)	
	tel_contato = models.CharField('Telefone Contato',max_length=11, unique = True,blank =True )	
	logradouro = models.CharField('Logradouro', max_length=200, blank=True)	
	numero = models.CharField('Número', max_length=5, blank=True)
	complemento = models.CharField('Complemento', max_length=100, blank=True)	
	cep = models.CharField('CEP', max_length=11, blank=True)	
	estado = models.CharField('Estado', choices=STATE_CHOICES,  max_length=2, blank=True)	
	cidade = models.CharField('Cidade',max_length=100, blank=True)	
	
	def __str__(self):
		return self.nome_banco

