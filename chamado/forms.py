from django import forms
from .models import Chamado

class ChamadoForm(forms.ModelForm):
    class Meta:
        models = Chamado
        fields = ['descricao','data_abertura','data_fechamento','solicitante'
                'tecnico_responsavel','equipamento','setor']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }
        