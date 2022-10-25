from django.contrib import admin
from .models import Funcionario, Filho

# Register your models here.

class FilhoAdmin(admin.TabularInline):
    model = Filho    
    # fieldsets = ('', {            
    #         'fields': ('nome_filho','data_nasc_filho')
    #     }),
    extra = 1

class FuncionarioAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cadastro', {
            'fields': ('empresa','nome', ('cargo','salario'),('nascimento',
             'naturalidade',),('admissao','banco'),'vtransporte',('residencial','celular'),('escolaridade','est_civil'),
             ('email','cpf'), ('ctps','pis'),('titulo','cnh'),('rg', 'data_rg'),('sexo','raca'),)
        }),
        ('Endereço', {
            'fields': (('logradouro','numero'),('complemento','cep'),('cidade','estado')),
        })
        
    )
    inlines = [
        FilhoAdmin,
    ]
admin.site.register(Funcionario, FuncionarioAdmin)