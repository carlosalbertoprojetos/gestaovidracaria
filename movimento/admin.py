from django.contrib import admin
from .models import Movimento, ProdutoMovimento

from financeiro.models import Compra, Venda


class ProdutoMovimentoAdmin(admin.TabularInline):
    model = ProdutoMovimento
    # fieldsets = (
    #     ('Contato', {
    #         'fields': (('cliente', 'responsavel'))
    #     }),
    #     ('Endereço', {
    #         'fields': (('logradouro_obra'),('numero_obra','complemento_obra'),('cep_obra','estado_obra','cidade_obra')),
    #     }),
    # )
    # readonly_fields = ('subtotal',)
    extra = 3
    ...


class MovimentoAdmin(admin.ModelAdmin):

    # readonly_fields = ('total',)
    inlines = [
        ProdutoMovimentoAdmin,
    ]

admin.site.register(Movimento, MovimentoAdmin)