from django import forms
from .models import Historico   

class HistoricoForm(forms.ModelForm):

    class Meta: 
        model = Historico
        fields = ['chamado','descricao','alterado_por','data_alteracao']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }