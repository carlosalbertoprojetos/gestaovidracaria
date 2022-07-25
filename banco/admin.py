from django.contrib import admin
from .models import Banco

# Register your models here.

class BancoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cadastro', {
            'fields': (('nome_banco', 'agencia'),('conta','pix','tel_contato', 'saldo'))
        }),
        ('Endereço', {
            'classes': ('collapse',),
            'fields': (('logradouro','numero','complemento'),('cep','estado','cidade')),
        }),
    )
       

admin.site.register(Banco, BancoAdmin)