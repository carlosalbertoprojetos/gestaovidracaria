from django.contrib import admin

from .models import Banco, CaixaDia


class BancoAdmin(admin.ModelAdmin):
    list_display = ('nome','agencia', 'conta','saldo_dia')

    model = Banco
    fieldsets = [
        ('Dados',{
            'fields':        
                (('nome','agencia', 'conta'),)              
        }), 
        ('Localização e contato',{
            'fields':        
                (('tel_contato','cep', 'cidade', 'estado'),)
        }),
        ('Chave PIX e saldo',{
            'fields':        
                (('pix','saldo_dia'),)
        }), 
    ]
    search_fields = ['nome', 'pix', 'cidade', 'estado']
    ordering = ('nome',)
admin.site.register(Banco, BancoAdmin) 


class CaixaDiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'agencia', 'conta', 'saldo_dia')

    model = CaixaDia
    fieldsets = [
        ('Dados',{
            'fields':        
                (('nome','agencia', 'conta'),)              
        }), 
        ('Localização e contato',{
            'fields':        
                (('tel_contato','cep', 'cidade', 'estado'),)
        }),
        ('Chave PIX e saldo',{
            'fields':        
                (('pix','saldo_dia'),)
        }), 
    ]
    search_fields = ['nome', 'pix', 'cidade', 'estado']
    ordering = ('nome',)
admin.site.register(CaixaDia, CaixaDiaAdmin) 
