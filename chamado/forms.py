from django import forms
from .models import Chamado

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['descricao','data_fechamento','solicitante',
                'tecnico_responsavel','equipamento','setor','status']
        widgets = {
            'data_fechamento': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }
        