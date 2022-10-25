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
    fieldsets = [
        ('Produto', {
            'fields': (('codigo','nome'), ('ncm','cst'),('cfop', 'mva'),
            ('categoria', 'fornecedor'),('valor_custo','valor_venda'), ('peso_barra','icms_1'),('ipi', 'icms_2'),
             'disponivel'),
        }),
        ('Detalhes', {
            'fields': ('unimed', 'quantidade','imagem', 'descricao')
        }),
    ]
    ordering = ('nome',)