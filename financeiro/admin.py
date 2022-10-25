import pdb
from django.contrib import admin
from django.utils.formats import number_format

from .models import Compra, CompraProduto, CompraPrestacao, Venda, VendaProduto, VendaPrestacao


class CompraProdutoAdmin(admin.TabularInline):
    model = CompraProduto
    fieldsets = (
        ('', {
            'fields': ('produto','quantidade', 'precoProduto', 'detalhes', 'subTotalProduto')
        }),
    ) 
    readonly_fields = ['precoProduto', 'subTotalProduto',]
    extra = 0


class CompraPrestacaoAdmin(admin.TabularInline):
    model = CompraPrestacao
    extra = 1
    ...


class CompraAdmin(admin.ModelAdmin):
    model = Compra
    fieldsets = (
        ('', {
            'fields': (('codigo','data', 'fornecedor'),('formapgto','status','totalCompra',),'imagem',)
        }),
    )
    readonly_fields = ('totalCompra',)
    inlines = [
        CompraPrestacaoAdmin,
        CompraProdutoAdmin,
    ]
    ordering = ('data',) 
    search_fields = ['data']
    ...
admin.site.register(Compra, CompraAdmin)


class VendaProdutoAdmin(admin.TabularInline):

    def get_valor_venda(self, obj):
        return "R$ %s" % number_format(obj.produto_valor_venda,2)

    model = VendaProduto
    fieldsets = (
        ('', {
            'fields': ('produto','quantidade', 'precoProduto', 'detalhes','get_valor_venda','subTotalProduto')
        }),
    )
    get_valor_venda.short_description = 'Valor de Venda'   
    readonly_fields = ['precoProduto', 'get_valor_venda','subTotalProduto',] 
    extra = 0


class VendaPrestacaoAdmin(admin.TabularInline):
    model = VendaPrestacao
    extra = 1
    ...


class VendaAdmin(admin.ModelAdmin):
    model = Venda
    fieldsets = (
        ('', {
            'fields': (('codigo', 'data', 'cliente'),('formapgto', 'status', 'totalVenda',))
        }),
    )    
    readonly_fields = ('totalVenda',)
    inlines = [
        VendaPrestacaoAdmin,
        VendaProdutoAdmin
        ] 
    ordering = ('data',) 
    search_fields = ['data']
    ...
admin.site.register(Venda, VendaAdmin)