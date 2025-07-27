from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome','patrimonio','setor','status']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }

