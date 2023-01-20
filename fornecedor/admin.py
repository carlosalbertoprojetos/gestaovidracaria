from django.contrib import admin
#from sympy import Complement
from .models import Fornecedor





class FornecedorAdmin(admin.ModelAdmin):
    fieldsets = (
        # ('Cadastro', {
        #     'fields': (('nome','contato'),('conta','tel_principal','tel_contato'), ('email','cnpj','insc_estadual'))
        # }),
        ('Cadastro', {
            'fields': (('nome','tel_contato'),('cnpj','insc_estadual',),('email'))
        }),
        ('Endereço', {            
            'fields': (('logradouro','numero'),('complemento','cep'),('cidade','estado')),
        }),
    )
    
    #inlines = [DadosBancariosAdmin,]
    search_fields = ['nome', 'cnpj']   
       

admin.site.register(Fornecedor, FornecedorAdmin)