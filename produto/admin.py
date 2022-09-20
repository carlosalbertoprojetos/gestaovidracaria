from django.contrib import admin

from .models import Categoria, Produto, UnidadeMedida


@admin.register(UnidadeMedida)
class UnitMeasurementAdmin(admin.ModelAdmin):
    ...


@admin.register(Categoria)
class CategoraAdmin(admin.ModelAdmin):
    model = Categoria
    ordering = ('nome',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    #list_display = ['categoria','fornecedor', 'nome','preco', 'valor','disponivel', 'estoque', 'descricao']
    #list_filter = ['categoria', 'nome', 'disponivel', 'created_at', 'updated']
    #search_fields = ('categoria', 'nome', 'disponivel')
    fieldsets = [
        ('Produto', {
            'fields': ('fornecedor', ('codigo', 'categoria', 'nome')),
        #         ('ncm','cst','cfop', 'mva'),('peso_barra','icms_1','ipi', 'icms_2')),
        }),
        ('Detalhes', {
            'fields': ('unimed', 'quant_produto', 'disponivel','descricao', 'imagem')
        }),
    ]
    
    ordering = ('nome',)
    
    