from django import forms

from apps.productos.models import Compra

class CompraForm(forms.ModelForm):

    class Meta:
        model = Compra

        fields = [
            'codigo',
        ]

        labels = {
            'codigo': 'Codigo de compra',
        }

        widgets = {
            'codigo' : forms.TextInput(attrs={'type':'text'}),
        }
