from django.contrib import admin
from django.utils.formats import number_format

from .models import (
    Compra, CompraProduto, CompraPrestacao, 
    Venda, VendaProduto, VendaPrestacao
)


class CompraProdutoAdmin(admin.TabularInline):
    model = CompraProduto
    readonly_fields = ('preco', 'subtotal',)
    extra = 3
    ...

class CompraPrestacaoAdmin(admin.TabularInline):
    model = CompraPrestacao
    extra = 1
    ...

class CompraAdmin(admin.ModelAdmin):
    model = Compra
    fieldsets = (
        ('Cadastro', {
            'fields': ('data', 'fornecedor',('formapgto','imagem', 'status'), ('pgto_avista', 'total'))
        }),
    )
    readonly_fields = ('total',)
    inlines = [
        CompraPrestacaoAdmin,
        CompraProdutoAdmin,
    ]
    ...
admin.site.register(Compra, CompraAdmin)


class VendaProdutoAdmin(admin.TabularInline):
    model = VendaProduto
    readonly_fields = ('preco', 'subtotal',)
    extra = 3
    ...

class VendaPrestacaoAdmin(admin.TabularInline):
    model = VendaPrestacao
    extra = 1
    ...


soma_total = 0
class VendaProdutoAdmin(admin.TabularInline):

    def get_valor_venda(self, obj):
        #global soma_total
        #pdb.set_trace()                 
        #subtotal = round(obj.produto.valor_venda * obj.quant_produto_venda,2)
        #soma_total += subtotal
        #print('Soma total',soma_total)
        return "R$ %s" % number_format(obj.produto.valor_venda,2)

    model = VendaProduto
    fieldsets = (
        ('', {
            'fields': ('produto','quant_produto_venda', 'detalhes_venda','get_valor_venda','subtotal')
        }),
    )      
    
    get_valor_venda.short_description = 'Valor de Venda'   
    #salvar no banco de dados tambem
    readonly_fields = ['get_valor_venda','subtotal',] 
    extra = 0











class VendaAdmin(admin.ModelAdmin):
    model = Venda
    fieldsets = (
        ('Cadastro', {
            'fields': ('cliente',('data', 'num_venda'), ('formapgto','imagem'), ('custo', 'status'), ('pgto_avista', 'total'))
        }),
    )
    readonly_fields = ('total',)
    inlines = [
        VendaPrestacaoAdmin,
        VendaProdutoAdmin,
    ]
    ...
    ordering = ('data_venda',) 
    search_fields = ['data_venda'] 
admin.site.register(Venda, VendaAdmin)
