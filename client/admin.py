from django.contrib import admin
#from sympy import Complement
from .models import Client

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     ('Cadastro', {
    #         'fields': ('name', 'cpf', 'email', 'phoneNumber', 'is_active')
    #     }),
    #     ('Endereço', {
    #         'classes': ('collapse',),
    #         'fields': ('street','number','complement','postal_code','state','city'),
    #     }),
    # )
    ...   

admin.site.register(Client, ClientAdmin)
