from django.contrib import admin
from .models import Fornecedor


class FornecedorAdmin(admin.ModelAdmin):
    fieldsets = (
        # ('Cadastro', {
        #     'fields': (('nome','contato'),('conta','tel_principal','tel_contato'), ('email','cnpj','insc_estadual'))
        # }),
        ('Cadastro', {
            'fields': (('nome','contato'),('conta'), ('email','cnpj','insc_estadual'))
        }),
        ('Endereço', {            
            'fields': (('logradouro','numero'),('complemento','cep'),('cidade','estado')),
        }),
    )
       

admin.site.register(Fornecedor, FornecedorAdmin)