from django.contrib import admin
from .models import Funcionario

# Register your models here.

class FuncionarioAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cadastro', {
            'fields': ('nome_empresa','nome_funcionario', 'data_admissao','banco','cargo','salario', 'data_nascimento',
             'naturalidade','vale_transporte','tel_residencial','tel_celular','escolaridade','estado_civil',
             'sexo','raca_cor','email','rg', 'data_rg','cpf', 'ctps','pis','titulo_eleitor','cnh')
        }),
        ('Endereço', {
            'classes': ('collapse',),
            'fields': ('logradouro','numero','complemento','cep','estado','cidade'),
        }),
        ('Filiação', {
            'classes': ('collapse',),
            'fields': ('nome_pai','nome_mae','nome_conjuge','nome_filho','data_nasc_filho'),
        }),
    )
       

admin.site.register(Funcionario, FuncionarioAdmin)