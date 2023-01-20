from django import forms
from django.forms.models import inlineformset_factory
import locale

from .models import Compra, CompraPrestacao, CompraProduto


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class CompraForm(forms.ModelForm):

    class Meta:
        model = Compra
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['num_prestacoes'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True



class CompraProdutoForm(forms.ModelForm):

    class Meta:
        model = CompraProduto
        fields = "__all__"
        exclude = ('preco', 'compra', 'subtotal')


class CompraPrestacaoForm(forms.ModelForm):

    class Meta:
        model = CompraPrestacao
        fields = "__all__"
        exclude = ('compra','parc_juros',)

FormsetFactory_produto = inlineformset_factory(Compra, CompraProduto, form=CompraProdutoForm, extra=1)
FormsetFactory_prestacao = inlineformset_factory(Compra, CompraPrestacao, form=CompraPrestacaoForm, extra=1)

FormsetFactory_produto_up = inlineformset_factory(Compra, CompraProduto, form=CompraProdutoForm, extra=0)
FormsetFactory_prestacao_up = inlineformset_factory(Compra, CompraPrestacao, form=CompraPrestacaoForm, extra=0)


class AnoForm(forms.Form):
    select_anos = CompraPrestacao.objects.dates('data_venc', 'year')
    ANO_CHOICES = []
    for p in select_anos:
        ANO_CHOICES.append(((p.strftime('%Y')),(p.strftime('%Y'))))

    ano =  forms.ChoiceField(
        choices=ANO_CHOICES,
        label='Ano')
    
    class Meta:
        fields = ('ano')

    def __init__(self, ano=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ano'].queryset = CompraPrestacao.objects.filter(data_venc__year=ano)
