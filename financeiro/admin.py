import pdb
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportMixin
from import_export import resources

from django.utils.formats import number_format

from .models import Compra, CompraProduto, CompraPrestacao, Venda, VendaProduto, VendaPrestacao


class CompraProdutoAdmin(admin.TabularInline):
    model = CompraProduto
    readonly_fields = ('preco', 'subtotal',)
    extra = 0
    ...

class CompraPrestacaoAdmin(admin.TabularInline):
    model = CompraPrestacao
    extra = 1
    ...

class CompraAdmin(admin.ModelAdmin):
    model = Compra
    fieldsets = (
        ('', {
            'fields': (('codigo', 'fornecedor'), ('data_compra'),('formapgto','status','total',),'imagem',)
        }),
    )
    readonly_fields = ('total',)
    inlines = [
        CompraPrestacaoAdmin,
        CompraProdutoAdmin,
    ]
    ...
admin.site.register(Compra, CompraAdmin)


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
    list_filter = ('data_venda',)
    fieldsets = (
        ('', {
            'fields': ('produto','quantidade', 'detalhes','get_valor_venda','subtotal')
        }),
    )      
    
    get_valor_venda.short_description = 'Valor de Venda'   
    #salvar no banco de dados tambem
    readonly_fields = ['get_valor_venda','subtotal',] 
    extra = 0


class VendaPrestacaoAdmin(admin.TabularInline):
    model = VendaPrestacao
    extra = 1
    ...


class VendaAdmin(ImportExportModelAdmin):    
    model = Venda
    
    #def get_custo_venda(self, obj):        
    #    obj.custo = soma_total
    #    print('Total = ', obj.custo)
    #    return soma_total
    #corrigir o valor do custo da venda
    #get_custo_venda.short_description = 'Custo da venda R$'
       
    fieldsets = (
        ('', {
            'fields': (('codigo', 'data_venda', 'cliente'),('formapgto', 'status',))
        }),
    )
    
    list_filter = ('data_venda',)
    #readonly_fields = ()
    inlines = [VendaProdutoAdmin]     
    #search_fields = ['codigo_venda']        
    ordering = ('data_venda',) 
    #search_fields = ['data_venda']     
admin.site.register(Venda, VendaAdmin)

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