from django import forms
from django.contrib.postgres.forms.ranges import DateRangeField,RangeWidget
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

from .models import EstoqueFisico


class EstoqueFisicoForm(forms.ModelForm):
 
    class Meta:
        model = EstoqueFisico
        fields = '__all__'
        exclude = ('estoque_atual',)

