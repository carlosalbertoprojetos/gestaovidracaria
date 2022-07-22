from django import forms

from .models import Produto


class ProdutoForm(forms.ModelForm):
    fieldsets = [
        ('Identificação', {'fields': [
            ('categoria', 'nome'),
        ]}),
        ('Detalhes', {'fields': [
            ('preco', 'disponivel', 'estoque'),
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




