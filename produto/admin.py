from django.contrib import admin

from .models import Categoria, UnidadeMedida, Produto, Tributos



class CategoriaAdmin(admin.ModelAdmin):
    ...

admin.site.register(Categoria, CategoriaAdmin)


class UnidadeMedidaAdmin(admin.ModelAdmin):
    ...

admin.site.register(UnidadeMedida, UnidadeMedidaAdmin)


class TributosAdmin(admin.StackedInline):
    # def get_valor_compra(self, obj):                
    #     return round(obj.tributos.valor_unitario(),2) 

    model = Tributos
    fieldsets = [
        ('Alíquotas',{
            'fields':        
                (('produto', 'valor_unitario', 'mva', 'taxa_icms_interno', 'taxa_icms_inter','taxa_ipi', 'taxa_frete', 'valor_frete'), 
             )
        }),
        ('Tributos',{
            'fields':        
                (('valor_barra_un', 'icms_interno', 'base_icms_st', 'icms_inter', 'ali_dif_icms','dif_aliq_icms', 'ipi', 'frete', 'base_calc_st', 'st', 'custo_final', 'custo_frac', 'preco_frac'),
             )
        }),
    ]
    readonly_fields = ['valor_barra_un', 'icms_interno', 'base_icms_st', 'icms_inter', 'ali_dif_icms','dif_aliq_icms', 'ipi', 'frete', 'base_calc_st', 'st', 'custo_final', 'custo_frac', 'preco_frac']
    # get_valor_compra.short_description = 'Valor do Produto R$'
    extra = 0
    ...


class ProdutoAdmin(admin.ModelAdmin):
    model = Produto   
    list_display = ('fornecedor', 'codigo', 'nome', 'categoria', 'descricao', 'status_disponivel')   
    fieldsets = [
            ('INFORMAÇÕES', {
                'fields': (('nome','fornecedor', 'codigo'),
                ('categoria', 'unimed', 'ncm', 'cst', 'cfop', 'peso_barra', 'estoque_ini'),
                'descricao',
                'status_disponivel', 
                ('criadoem', 'atualizadoem')
                )
            }),
    ]
    readonly_fields = ['criadoem', 'atualizadoem']
    inlines = [TributosAdmin]

admin.site.register(Produto, ProdutoAdmin)


# class CalculosAdmin(admin.ModelAdmin):
#     list_display = ('tributos', 'valor_barra_un', 'icms_interno', 'base_icms_st', 'icms_inter', 'ali_dif_icms', 'dif_aliq_icms', 'ipi', 'frete', 'base_calc_st', 'st', 'custo_final', 'custo_frac', 'preco_frac')
#     readonly_fields = ['valor_barra_un', 'icms_interno', 'base_icms_st', 'icms_inter', 'ali_dif_icms', 'dif_aliq_icms', 'ipi', 'frete', 'base_calc_st', 'st', 'custo_final', 'custo_frac', 'preco_frac']

#     ...

# admin.site.register(Calculos, CalculosAdmin)
