from django import forms

from apps.productos.models import Compra

class CompraForm(forms.ModelForm):

    class Meta:
        model = Compra

        fields = [
            'tabladetalle',
            'importe',
            'cliente',
            'nitems',
        ]

        labels = {
            'tabladetalle': 'Tabla de detalle',
            'importe': 'Importe',
            'cliente': 'Cliente',
            'nitems': 'Numero de Items',
        }

        widgets = {
            'tabladetalle': forms.TextInput(attrs={'type':'text'}),
            'importe': forms.TextInput(attrs={'type':'tel'}),
            'cliente': forms.TextInput(attrs={'type':'tel'}),
            'nitems': forms.TextInput(attrs={'type':'tel'}),
        }
