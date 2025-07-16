from django import forms
from .models import Historico   

class HistoricoForm(forms.ModelForm):

    class Meta: 
        model = Historico
        fields = ['chamado','status_anterior','status_novo','alterado_por']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }