from django.contrib import admin
from .models import Movimento, ProdutoMovimento

from financeiro.models import Compra, Venda


class ProdutoMovimentoAdmin(admin.TabularInline):
    model = ProdutoMovimento
    extra = 3
    ...


class MovimentoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cadastro', {
            'fields': ('funcionario',('data', 'operacao'),('total', 'status'), 'local')
        }),
    )
    readonly_fields = ('total',)     
    inlines = [
        ProdutoMovimentoAdmin,
    ]
admin.site.register(Movimento, MovimentoAdmin)