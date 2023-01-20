from django.contrib import admin


from .models import Venda, VendaProduto, VendaPrestacao


class VendaProdutoAdmin(admin.TabularInline):
    model = VendaProduto
    list_filter = ('data_venda',)
    fieldsets = (
        ('', {
            'classes': ['grp-collapse grp-closed'],
            'fields': (('produto','quantidade'),
             'status')
        }),
    )
    extra = 0


class VendaPrestacaoAdmin(admin.StackedInline):
    model = VendaPrestacao
    fieldsets = (
        ('', {
            'fields': (('num_parcela', 'data_venc','data_pgto',),('valor_parc','formapgto','detalhes'),
            ('banco','status'))
        }),
    )
    extra = 0


class VendaAdmin(admin.ModelAdmin):
    model = Venda
    list_display = ('data_venda', 'nota_fs', 'cliente', 'custo_total', 'desconto_venda', 'num_parcelas', 'vlr_parcelas')

    fieldsets = (
        ('INFORMAÇÕES', {
            'fields': (('data_venda','nota_fs'),
                        ('cliente','codigo'),
                        ('custo_total', 'desconto_venda'),
                        ('num_parcelas', 'vlr_parcelas')
                        )
        }),
    )
    readonly_fields = ['custo_total', 'num_parcelas', 'vlr_parcelas']    
    inlines = [VendaProdutoAdmin, VendaPrestacaoAdmin]

admin.site.register(Venda, VendaAdmin)