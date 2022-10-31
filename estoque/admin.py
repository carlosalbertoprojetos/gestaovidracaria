from django.contrib import admin

#from import_export.admin import ImportExportModelAdmin
#from import_export.admin import ImportExportMixin
#from import_export import resources

from .models import Fisico, Fiscal
'''
@admin.register(Produto)
class ProductAdmin(admin.ModelAdmin):
    ordering = ['product']
    list_display = (
        'ncm', 'imported', 'product', 'brand', 'get_price', 'outofline')
    list_filter = ('outofline', 'brand',)
    search_fields = ('product',)
'''

@admin.register(Fisico)
class FisicoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto','codigo_produto', 'estoque_inicial', 'unidade_medida',
    'custo_fracionado','valor_total_custo',) 
    '''
    fieldsets = [
        ('Produto', {
            'fields':
             (('fornecedor'),
             ('compra', 'venda',), 'produto', )
        }),
        ('Valores calculados (R$)',{
            'classes': ['grp-collapse grp-closed'],
            'fields':        
                ((),
                (), 
             )
        }),
    ]
'''

class FiscalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fiscal, FiscalAdmin)

'''

from import_export.admin import ImportExportModelAdmin

from .models import Categoria, Produto, UnidadeMedida


@admin.register(UnidadeMedida)
class UnitMeasurementAdmin(admin.ModelAdmin):
    ...

@admin.register(Categoria)
class CategoraAdmin(admin.ModelAdmin):
    model = Categoria
    ordering = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(ImportExportModelAdmin):    
    fieldsets = [
        ('Produto', {
            'fields':
             (('codigo','nome'),
             ('categoria', 'fornecedor',),'status')
        }),
        ('Códigos fiscais',{
            'classes': ['grp-collapse grp-closed'],
            'fields':        
                (('ncm','cst'),
                ('cfop', 'mva'), 
             )
        }),
        
        ('Valores e taxas', {
            'classes': ['grp-collapse grp-closed'],
            'fields':
                (('valor_custo','valor_venda'),
                ('peso_barra','aliquota_1'),
                ('ipi', 'aliquota_2'), ('taxa_frete','valor_frete')),             
        }),
        
        ('Detalhes', {
            'classes': ['grp-collapse grp-closed'],
            'fields': 
                ('unimed', 'quantidade','imagem', 'descricao')
        }),

        ('Valores calculados (R$)', {
            'classes': ['grp-collapse grp-closed',],
            'fields': 
                (('valor_venda_produto','icms_interno_1', 'calculo_icms_st', 'icms_interno_2'),
                ('diferenca_aliquota_icms','calculo_ipi','calculo_frete','base_calculo_st'),                
                 ('calculo_st', 'calculo_preco_final',
                'custo_fracionado_produto','custo_venda_fracionada',))
        }),
    ]
    
    ordering = ('nome',)
    readonly_fields = ['valor_venda_produto', 'icms_interno_1', 
                        'calculo_ipi', 'calculo_frete','calculo_icms_st', 
                        'icms_interno_2', 'base_calculo_st','calculo_st',
                        'diferenca_aliquota_icms', 'calculo_preco_final',
                        'custo_fracionado_produto','custo_venda_fracionada'] 
'''
