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
            'fields': ('data', ('fornecedor','formapgto',), ('status','total',),'imagem',)
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
            'fields': (('num_venda'),('data', 'cliente','formapgto'),('custo', 'status', 'total',))
        }),
    )
    readonly_fields = ('total',)
    inlines = [
        VendaProdutoAdmin,
    ]
    ...
admin.site.register(Venda, VendaAdmin)