from django.contrib import admin
from .models import Fornecedor


class FornecedorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cadastro', {
            'fields': (('nome','contato'),('conta','tel_principal','tel_contato'), ('email','cnpj','insc_estadual'))
        }),
        ('Endereço', {
            'classes': ('collapse',),
            'fields': (('logradouro'),('numero','complemento'),('cep','estado','cidade')),
        }),
    )
       

admin.site.register(Fornecedor, FornecedorAdmin)