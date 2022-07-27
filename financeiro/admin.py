from django.contrib import admin

from .models import Compra, Venda

from financeiro.models import CompraProduto


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


# class VendaProdutoAdmin(admin.TabularInline):
#     model = Venda
#     readonly_fields = ('subtotal',)
#     extra = 3
#     ...


# class Admin(admin.ModelAdmin):

#     readonly_fields = ('total',)
#     inlines = [
#         VendaProdutoAdmin,
#     ]

# admin.site.register(Venda, VendaProdutoAdmin)