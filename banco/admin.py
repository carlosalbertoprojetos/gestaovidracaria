from django.contrib import admin
from .models import Banco

# Register your models here.

class BancoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cadastro', {
            'fields': (('nome_banco', 'agencia'),('conta','saldo'),('tel_contato','pix'))
        }),
        ('Endereço', {            
            'fields': (('logradouro','numero'),('complemento','cep'),('cidade', 'estado')),
        }),
    )       

admin.site.register(Banco, BancoAdmin)