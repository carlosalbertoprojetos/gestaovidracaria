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
    list_display = ['categoria', 'nome','preco','disponivel', 'estoque', 'descricao']
    list_filter = ['categoria', 'nome', 'disponivel', 'created_at', 'updated']
    search_fields = ('categoria', 'nome', 'disponivel')
    fieldsets = [
        ('Produto', {
            'fields': ('categoria', 'nome', ('preco', 'disponivel', 'estoque',)),
        }),
        ('Detalhes', {
            'fields': ('unimed', 'descricao',)
        }),
    ]
    ordering = ('nome',)
    readonly_fields = ['estoque',]

