from django.contrib import admin

from .models import Compra, Venda

from produto.models import Produto


class CompraProdutoAdmin(admin.TabularInline):
    model = Produto
    # readonly_fields = ('subtotal',)
    extra = 3
    ...


class CompraAdmin(admin.ModelAdmin):

    # readonly_fields = ('total',)
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