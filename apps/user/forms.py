from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext, ugettext_lazy as _
from django.forms import Field
from django.utils.translation import ugettext_lazy



class RegistroForm(UserCreationForm):
    #some_field = forms.CharField(error_messages=my_default_errors)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    #some_field = forms.CharField(error_messages=my_default_errors)
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
        ]

        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Repita la contraseña',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Email',
        }
