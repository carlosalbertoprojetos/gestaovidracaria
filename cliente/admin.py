from django.contrib import admin
from .models import Cliente, Obra


# class ObraAdmin(admin.TabularInline):
class ObraAdmin(admin.StackedInline):
    model = Obra
    fieldsets = (
        ('Contato', {
            'fields': (('cliente', 'responsavel'))
        }),
        ('Endereço', {
            'fields': (('logradouro_obra','numero_obra'),('complemento_obra', 'cep_obra'),('cidade_obra','estado_obra')),
        }),
    )
    extra = 0


class ClienteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cadastro', {
            'fields': (('cliente', 'contato'),('tel_principal','tel_contato'), ('email','cpf'),('cnpj', 'insc_estadual'))
        }),
        ('Endereço', {            
            'fields': (('logradouro','numero'),('complemento','cep'),('cidade','estado')),
        }),
    )
    inlines = [
        ObraAdmin,
    ]

admin.site.register(Cliente, ClienteAdmin)
