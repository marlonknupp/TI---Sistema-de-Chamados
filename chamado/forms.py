from django import forms
from .models import Chamado

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['descricao','data_abertura','data_fechamento','solicitante',
                'tecnico_responsavel','equipamento','setor','status','prioridade']
        widgets = {
            'data_abertura': forms.DateInput(attrs={'type': 'date'}),
            'data_fechamento': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }
        