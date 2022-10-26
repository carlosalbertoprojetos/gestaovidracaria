from django.contrib import admin
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