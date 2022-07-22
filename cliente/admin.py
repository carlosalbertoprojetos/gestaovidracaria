from django.contrib import admin
from .models import Cliente, Obra



class ObraAdmin(admin.StackedInline):
    model = Obra
    fieldsets = (
        ('Contato', {
            'fields': (('cliente', 'responsavel'))
        }),
        ('Endereço', {
            'fields': (('logradouro_obra'),('numero_obra','complemento_obra'),('cep_obra','estado_obra','cidade_obra')),
        }),
    )
    extra = 0
    ...


class ClienteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cadastro', {
            'fields': (('num_venda'),('nome_cliente', 'nome_contato'),('tel_principal','tel_contato', 'email'), ('cpf', 'cnpj', 'insc_estadual'))
        }),
        ('Endereço', {
            'classes': ('collapse',),
            'fields': (('logradouro'),('numero','complemento'),('cep','estado','cidade')),
        }),
    )
    inlines = [
        ObraAdmin,
    ]

admin.site.register(Cliente, ClienteAdmin)
