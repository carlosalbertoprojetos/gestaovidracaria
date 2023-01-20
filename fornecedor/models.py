from django.db import models

STATE_CHOICES = (
		('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'),
		('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'),
		('MG','MG'), ('PA','PA'), ('PB','PB'), ('PE','PE'), ('PI','PI'), ('PR','PR'), 
		('RJ','RJ'), ('RN','RN'), ('RO','RO'), ('RR','RR'), ('RS','RS'), ('SC','SC'), 
		('SE','SE'), ('SP','SP'), ('TO','TO'),
    
    )

class Fornecedor(models.Model):	
	
	nome = models.CharField('Fornecedor',max_length=200,)
	tel_principal = models.CharField('Telefone Principal',max_length=11, blank = True)
	tel_contato = models.CharField('Telefone Contato',max_length=11, blank = True)
	email = models.EmailField('E-mail', max_length=254, blank=True)	
	cnpj = models.CharField('CNPJ',max_length=18, blank = True)
	insc_estadual = models.CharField('Inscrição Estadual',max_length=15, blank=True)
	logradouro = models.CharField('Logradouro', max_length=200, blank=True,)
	numero = models.CharField('Número', max_length=30, blank=True)
	complemento = models.CharField('Complemento', max_length=100, blank=True)
	cep = models.CharField('CEP', max_length=11, blank=True)
	estado = models.CharField('Estado', choices=STATE_CHOICES,max_length=2, blank=True)
	cidade = models.CharField('Cidade',max_length=100, null=True, blank=True,)
	#nome = models.CharField('Banco/Refência',max_length=30,
	#validators=[RegexValidator('([A-Z])\w+',
    #                           'Somente letras maiúsculas.')], blank=True,)
    #agencia = models.CharField('Agência',max_length=30, blank=True)
    #conta = models.CharField('Conta',max_length=30, blank=True)
    #pix = models.CharField('Chave PIX',max_length=30, blank=True) 	
	
	class Meta:
		ordering = ['nome', ]
		verbose_name = 'Fornecedor'
		verbose_name_plural = 'Fornecedores'	

	def __str__(self):
		return self.nome
