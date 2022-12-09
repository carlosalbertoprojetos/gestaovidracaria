# from django import forms
# from django.forms import inlineformset_factory


# from .models import Movimento, ProdutoMovimento

# class MovimentoForm(forms.ModelForm):
#     class Meta:
#         model = Movimento
#         # fields = ['data', 'status', 'formpayment', 'withdraw', 'total']
#         fields = '__all__'
#     #     widgets = {
#     #         'data': forms.DateInput(attrs={'class': 'date'}), 
#     #         'status': forms.Select(attrs={'class': 'form-control', 'style':'width:70%'}),
#     #         'formpayment': forms.Select(attrs={'class': 'form-control','style':'width:80%'}),
#     #         'withdraw': forms.CheckboxInput(attrs={'class': ''}),
#     #     }

#     # def __init__(self, *args, **kwargs):
#     #     super(OrderForm, self).__init__(*args, **kwargs)
#     #     self.fields['total'].widget.attrs['readonly'] = True



# ProdutoMovimento_factory = inlineformset_factory(Movimento, ProdutoMovimento, form=ProdutoMovimento, extra=3) 