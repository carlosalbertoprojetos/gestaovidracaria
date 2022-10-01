from django.contrib import admin
from .models import (
    Compra, CompraProduto, CompraPrestacao, 
    Venda, VendaProduto, VendaPrestacao
)


class CompraProdutoAdmin(admin.TabularInline):
    model = CompraProduto
    readonly_fields = ('preco', 'subtotal',)
    extra = 3
    ...

class CompraPrestacaoAdmin(admin.TabularInline):
    model = CompraPrestacao
    extra = 1
    ...

class CompraAdmin(admin.ModelAdmin):
    model = Compra
    fieldsets = (
        ('Cadastro', {
            'fields': ('data', 'fornecedor',('formapgto','imagem', 'status'), ('pgto_avista', 'total'))
        }),
    )
    readonly_fields = ('total',)
    inlines = [
        CompraPrestacaoAdmin,
        CompraProdutoAdmin,
    ]
    ...
admin.site.register(Compra, CompraAdmin)


class VendaProdutoAdmin(admin.TabularInline):
    model = VendaProduto
    readonly_fields = ('preco', 'subtotal',)
    extra = 3
    ...

class VendaPrestacaoAdmin(admin.TabularInline):
    model = VendaPrestacao
    extra = 1
    ...

class VendaAdmin(admin.ModelAdmin):
    model = Venda
    # fieldsets = (
    #     ('Cadastro', {
    #         'fields': (('data', 'num_venda'), 'cliente',('formapgto','custo', 'status'), 'total', 'pgto_avista',)
    #     }),
    # )
    fieldsets = (
        ('Cadastro', {
            'fields': ('cliente',('data', 'num_venda'), ('formapgto','imagem'), ('custo', 'status'), ('pgto_avista', 'total'))
        }),
    )
    readonly_fields = ('total',)
    inlines = [
        VendaPrestacaoAdmin,
        VendaProdutoAdmin,
    ]
    ...
admin.site.register(Venda, VendaAdmin)
