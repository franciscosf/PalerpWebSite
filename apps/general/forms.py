from django import forms

from apps.general.models import PosibleCliente

class PosibleClienteForm(forms.ModelForm):

    class Meta:
        model = PosibleCliente

        fields = [
            'RUC',
            'nombre',
            'email',
            'telefono',
        ]

        labels = {
            'RUC' : 'RUC',
            'nombre' : 'Nombre',
            'email' : 'Email',
            'telefono' : 'Telefono',
        }

        widgets = {
            'RUC' : forms.TextInput(attrs={'type':'tel'}),
            'nombre' : forms.TextInput(attrs={'type':'text'}),
            'email' : forms.TextInput(attrs={'type':'email'}),
            'telefono' : forms.TextInput(attrs={'type':'tel'}),            
        }
