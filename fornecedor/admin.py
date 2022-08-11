from django.contrib import admin
from .models import Fornecedor

# Register your models here.

class FornecedorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cadastro', {
            'fields': (('nome_fornecedor','nome_contato'),('cnpj','insc_estadual'),('tel_principal','tel_contato'),('email', 'banco'))
        }),
        ('Endereço', {            
            'fields': (('logradouro','numero'),('complemento','cep'),('cidade','estado')),
        }),
    )
       

admin.site.register(Fornecedor, FornecedorAdmin)

