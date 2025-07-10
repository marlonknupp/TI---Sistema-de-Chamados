from django import forms
from .models import Setor

class SetorForm(forms.Modelform):
    class Meta:
        models = Setor
        fields = ['nome','andar']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }