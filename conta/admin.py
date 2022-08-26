from django.contrib import admin
from .models import Conta

# Register your models here.

class ContaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cadastro', {
            'fields': (('nome', 'agencia'),('conta','pix','tel_contato', 'saldo'))
        }),
        ('Endereço', {
            'classes': ('collapse',),
            'fields': (('logradouro','numero','complemento'),('cep','estado','cidade')),
        }),
    )
       

admin.site.register(Conta, ContaAdmin)