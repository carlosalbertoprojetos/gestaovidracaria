from django import forms
from django.contrib.postgres.forms.ranges import DateRangeField,RangeWidget
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

from .models import Funcionario, Filho


class FuncionarioForm(forms.ModelForm):
 
    class Meta:
        model = Funcionario
        fields = '__all__'

class FilhoForm(forms.ModelForm):

    #date_init = DateRangeField(widget=RangeWidget(AdminDateWidget()))    

    class Meta:
        model = Filho
        fields = "__all__"
        exclude = ('funcionario',)
        widgets = {

            "date_init": AdminDateWidget(),
            "date_fin": AdminDateWidget(),
            #"season": forms.HiddenInput(),            
        }