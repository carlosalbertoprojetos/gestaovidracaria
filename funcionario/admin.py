from django.contrib import admin
from .models import Funcionario, Filho

# Register your models here.

class FilhoAdmin(admin.StackedInline):
    model = Filho
    
    fieldsets = ('', {            
            'fields': ('nome_filho','data_nasc_filho'),
        }),
    extra = 0    

class FuncionarioAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cadastro', {
            'fields': ('nome_empresa','nome_funcionario', 'data_admissao',('banco','cargo','salario'), ('data_nascimento',
             'naturalidade'),'vale_transporte',('tel_residencial','tel_celular'),'escolaridade',('estado_civil',
             'sexo','raca_cor'),('rg', 'data_rg', 'email'),('cpf', 'ctps','pis','titulo_eleitor','cnh'))
        }),
        ('Endereço', {
            'classes': ('collapse',),
            'fields': (('logradouro'),('numero','complemento'),('cep','estado','cidade')),
        })
        
    )
    inlines = [
        FilhoAdmin,
    ]

admin.site.register(Funcionario, FuncionarioAdmin)