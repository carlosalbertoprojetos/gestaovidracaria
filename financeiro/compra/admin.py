from django.contrib import admin

from .models import Compra, CompraProduto, CompraPrestacao


class CompraProdutoAdmin(admin.TabularInline):
    def get_valor_compra(self, obj):                
        return round(obj.produto.calculo_preco_final(),2) 

    model = CompraProduto
    fieldsets = [
        ('Parcelas',{
            'classes': ['grp-collapse grp-closed'],
            'fields':        
                (('produto','quantidade', 'get_valor_compra', 'subtotal', 'status',), 
             )
        }),       
    ]
    readonly_fields = ['get_valor_compra', 'subtotal',]
    get_valor_compra.short_description = 'Valor do Produto R$'
    extra = 0
    ...


class CompraPrestacaoAdmin(admin.StackedInline):
    model = CompraPrestacao
    fieldsets = (
        ('', {
            'fields': (('num_parcela','data_venc','data_pgto'),('valor_parc', 'juros'), 
            ('parc_juros', 'formapgto', 'banco', 'status'))
        }),
    )
    readonly_fields = ['parc_juros',]
    extra = 0    


class CompraAdmin(admin.ModelAdmin):        
    model = CompraPrestacao   
    list_display = ('fornecedor', 'nota_fs', 'data_compra', 'codigo', 'status_compra', 'num_prestacoes', 'total')   
    fieldsets = [
            ('INFORMAÇÕES', {
                'fields': (('data_compra','nota_fs'),
                ('fornecedor', 'codigo'),
                'status_compra',
                ('num_prestacoes',
                'total'))
            }),
    ]
    readonly_fields = ['num_prestacoes', 'total']
    inlines = [CompraProdutoAdmin,CompraPrestacaoAdmin]

admin.site.register(Compra, CompraAdmin)