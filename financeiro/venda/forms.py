from django import forms
from django.forms.models import inlineformset_factory

from .models import Venda, VendaPrestacao, VendaProduto


class VendaForm(forms.ModelForm):
 
    class Meta:
        model = Venda
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['custo_total'].widget.attrs['readonly'] = True
        self.fields['num_parcelas'].widget.attrs['readonly'] = True
        self.fields['vlr_parcelas'].widget.attrs['readonly'] = True


class VendaProdutoForm(forms.ModelForm):

    #date_init = DateRangeField(widget=RangeWidget(AdminDateWidget()))    

    class Meta:
        model = VendaProduto
        fields = "__all__"
        exclude = ('venda','preco')
        # widgets = {

        #     "date_init": AdminDateWidget(),
        #     "date_fin": AdminDateWidget(),
        #     #"season": forms.HiddenInput(),            
        # }        


class VendaPrestacaoForm(forms.ModelForm):

    #date_init = DateRangeField(widget=RangeWidget(AdminDateWidget()))    

    class Meta:
        model = VendaPrestacao
        fields = "__all__"
        exclude = ('venda',)
        # widgets = {

        #     "date_init": AdminDateWidget(),
        #     "date_fin": AdminDateWidget(),
        #     #"season": forms.HiddenInput(),            
        # }


FormsetFactory_produto = inlineformset_factory(Venda, VendaProduto, form=VendaProdutoForm, extra=1)
FormsetFactory_prestacao = inlineformset_factory(Venda, VendaPrestacao, form=VendaPrestacaoForm, extra=1)

FormsetFactory_produto_up = inlineformset_factory(Venda, VendaProduto, form=VendaProdutoForm, extra=0)
FormsetFactory_prestacao_up = inlineformset_factory(Venda, VendaPrestacao, form=VendaPrestacaoForm, extra=0)


class AnoForm(forms.Form):
    select_anos = VendaPrestacao.objects.dates('data_venc', 'year')
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
        self.fields['ano'].queryset = VendaPrestacao.objects.filter(data_venc__year=ano)
