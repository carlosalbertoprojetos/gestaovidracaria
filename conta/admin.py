from django.contrib import admin
from .models import Conta

# Register your models here.

class ContaAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ('Cadastro', {
            'fields': (('nome', 'agencia'),('conta','pix'),('tel_contato', 'format_saldo'))
        }),
        ('Endereço', {            
            'fields': (('logradouro','numero'),('complemento','cep'),('cidade', 'estado')),
        }),
    )
    
    # self.format_saldo.short_description = 'Saldo'
    readonly_fields = ('format_saldo',)

admin.site.register(Conta, ContaAdmin)