from django import forms
from django.contrib.postgres.forms.ranges import DateRangeField,RangeWidget
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.forms.models import inlineformset_factory

from .models import Produto, Tributos, UnidadeMedida, Categoria

class UnidadeMedidaForm(forms.ModelForm): 
    class Meta:
        model = UnidadeMedida
        fields = '__all__'

class CategoriaForm(forms.ModelForm): 
    class Meta:
        model = Categoria
        fields = '__all__'        


class ProdutoForm(forms.ModelForm): 
    class Meta:
        model = Produto
        fields = '__all__'


class TributosForm(forms.ModelForm):
    #date_init = DateRangeField(widget=RangeWidget(AdminDateWidget()))    

    class Meta:
        model = Tributos
        fields = ('valor_unitario', 'taxa_icms_interno', 'taxa_icms_inter', 'mva', 'ipi', 'taxa_frete', 'valor_frete')
        # exclude = ('produto',)
        # widgets = {
        #     "date_init": AdminDateWidget(),
        #     "date_fin": AdminDateWidget(),
        #     #"season": forms.HiddenInput(),            
        # }

FormsetFactory = inlineformset_factory(Produto, Tributos, form=TributosForm, extra=0, min_num=1, can_delete=False)
