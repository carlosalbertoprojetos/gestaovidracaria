from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import User


class CustomSignupForm(SignupForm):

    option = forms.CharField(
        label=_('Opção'),
        widget=forms.Select
    )

    def clean_password1(self):
        password = self.data.get('password1')
        lpassword = len(password)

        if lpassword < 8 or lpassword > 16:
            raise ValidationError('A senha deve ter de 8 a 16 caracteres')

        if not any(char.isdigit() for char in password):
            raise ValidationError('A senha deve conter pelo menos 1 dígito')

        if not any(char.isalpha() for char in password):
            raise ValidationError('A senha deve conter pelo menos 1 letra')

        return password

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.option = self.cleaned_data.get('option')
        user.save()
        return user


class SignupAgentForm(UserCreationForm):

    email = forms.EmailField(
        required=True, help_text='Campo obrigatório! Insira um email válido!')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Este email já está cadastrado, por favor insira outro.')
        return email

    def clean_password1(self):
        password = self.data.get('password1')
        lpassword = len(password)

        if lpassword < 8 or lpassword > 16:
            raise ValidationError('A senha deve ter de 8 a 16 caracteres')

        if not any(char.isdigit() for char in password):
            raise ValidationError('A senha deve conter pelo menos 1 dígito')

        if not any(char.isalpha() for char in password):
            raise ValidationError('A senha deve conter pelo menos 1 letra')
        return password

    def save(self, commit=True):
        user = super(SignupAgentForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'is_active']

# class PhoneFormSet(forms.Form):

#     class Meta:
#         model = Contact
#         fields = '__all__'

#     def clean_cel_phone(self):
#         data = self.cleaned_data['cel_phone']
#         return sanitize_number(data)

#     def save(self, commit=False):
#         instance = super().save(commit=commit)
#         instance.save()
#         return instance


# class SocialFormSet(forms.Form):

#     class Meta:
#         model = SocialMedia
#         fields = '__all__'

#     def save(self, commit=False):
#         instance = super().save(commit=commit)
#         instance.save()
#         return instance
