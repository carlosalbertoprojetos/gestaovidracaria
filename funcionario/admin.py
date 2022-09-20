from django.contrib import admin
from .models import Funcionario, Filho

# Register your models here.

class FilhoAdmin(admin.StackedInline):
    model = Filho
    
    fieldsets = ('', {            
            'fields': ('nome_filho','data_nasc_filho')
        }),
    extra = 1    

class FuncionarioAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cadastro', {
            'fields': ('nome_empresa','nome_funcionario', ('cargo','salario'),('data_nascimento',
             'naturalidade',),('data_admissao','banco'),'vale_transporte',('tel_residencial','tel_celular'),('escolaridade','estado_civil'),
             ('email','cpf'), ('ctps','pis'),('titulo_eleitor','cnh'),('rg', 'data_rg'),('sexo','raca_cor'),)
        }),
        ('Endereço', {            
            'fields': (('logradouro','numero'),('complemento','cep'),('cidade','estado')),
        })
        
    )
    inlines = [
        FilhoAdmin,
    ]

admin.site.register(Funcionario, FuncionarioAdmin)