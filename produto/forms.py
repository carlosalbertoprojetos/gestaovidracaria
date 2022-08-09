from django import forms

from .models import Produto


class ProdutoForm(forms.ModelForm):
    fieldsets = [
        ('Identificação', {'fields': [
            ('categoria', 'fornecedor','codigo','nome', 'ncm', 'cst', 'cfop', 'peso_barra',
                'icms_1','icms_2', 'ipi', 'mva'),
        ]}),
        ('Detalhes', {'fields': [
            ('preco','disponivel', 'estoque'),
            'descricao', 
        ]}),
        
        ('Controle', {'fields': [
            'created_at',
            'updated',
        ]}),
    ]

    class Meta:
        model = Produto
        fields = '__all__'
        # exclude = ['user',]
        readonly_fields = ['created_at', 'updated_at']
