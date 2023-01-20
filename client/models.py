from django.db import models


from tourproject.constantes import STATE_CHOICES


class Client(models.Model):	
	nome_contato = models.CharField('Nome Completo',max_length=200,)
	#cpf = CPFField(masked=True)  # To enable auto-mask xxx.xxx.xxx-xx
	tel_principal = models.CharField('Telefone Principal',max_length=11, blank = True)
	tel_contato = models.CharField('Telefone Contato',max_length=11, blank = True)
	email = models.EmailField('E-mail', max_length=254, blank=True)
	cpf = models.CharField('CPF', max_length=14, blank = True)
	cnpj = models.CharField('CNPJ',max_length=18, blank = True)
	insc_estadual = models.CharField('Inscrição Estadual',max_length=15,blank = True)
	logradouro = models.CharField('Logradouro', max_length=200, blank=True,)
	numero = models.CharField('Número', max_length=30,blank=True)
	complemento = models.CharField('Complemento', max_length=100, blank=True)
	cep = models.CharField('CEP', max_length=11,blank=True)
	estado = models.CharField('Estado', choices = STATE_CHOICES, max_length=2, blank=True)
	cidade = models.CharField('Cidade',max_length=100,blank=True,)	
	#is_active = models.BooleanField('Ativar',default=True)

	class Meta:
		verbose_name = 'Cliente'
		verbose_name_plural = "Clientes"
	
	def __str__(self):
		return self.nome_contato

class Obra(models.Model):
    cliente = models.ForeignKey(Client, on_delete=models.DO_NOTHING, verbose_name='Cliente')
    responsavel = models.CharField('Responsável da Obra', max_length=200)
    logradouro = models.CharField('Logradouro', max_length=200, blank=True)
    numero = models.CharField('Número', max_length=30, blank=True)
    complemento = models.CharField('Complemento', max_length=100,blank=True)
    cep = models.CharField('CEP', max_length=11, blank=True)
    estado = models.CharField('Estado', choices=STATE_CHOICES,max_length=2, blank=True)
    cidade = models.CharField('Cidade',max_length=100, blank=True)

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = "Obra"
    
    def __str__(self):
        return self.responsavel
		