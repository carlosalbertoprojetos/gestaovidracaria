from django.contrib import admin

from .models import Compra, Venda, CompraProduto, VendaProduto


class CompraProdutoAdmin(admin.TabularInline):
    model = CompraProduto
    readonly_fields = ('preco', 'subtotal',)
    extra = 3
    ...


class CompraAdmin(admin.ModelAdmin):
    model = Compra
    fieldsets = (
        ('Cadastro', {
            'fields': ('data', 'fornecedor',('formapgto','imagem', 'status'), 'total',)
        }),
    )
    readonly_fields = ('total',)
    inlines = [
        CompraProdutoAdmin,
    ]
    ...
admin.site.register(Compra, CompraAdmin)


class VendaProdutoAdmin(admin.TabularInline):
    model = VendaProduto
    readonly_fields = ('preco', 'subtotal',)
    extra = 3
    ...


class VendaAdmin(admin.ModelAdmin):
    model = Venda
    fieldsets = (
        ('Cadastro', {
            'fields': (('data', 'num_venda'), 'cliente',('formapgto','custo', 'status'), 'total',)
        }),
    )
    readonly_fields = ('total',)
    inlines = [
        VendaProdutoAdmin,
    ]
    ...
admin.site.register(Venda, VendaAdmin)