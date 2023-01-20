from django import forms
from django.contrib.postgres.forms.ranges import DateRangeField,RangeWidget
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

from .models import Client, Obra


class ClientForm(forms.ModelForm):
 
    class Meta:
        model = Client
        fields = '__all__'

class ObraForm(forms.ModelForm):

    #date_init = DateRangeField(widget=RangeWidget(AdminDateWidget()))    

    class Meta:
        model = Obra
        fields = "__all__"
        exclude = ('cliente',)
        widgets = {

            "date_init": AdminDateWidget(),
            "date_fin": AdminDateWidget(),
            #"season": forms.HiddenInput(),            
        }