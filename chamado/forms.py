from django import forms
from django.contrib.auth.models import Group
from .models import Chamado
from usuario.models import Usuario  # importa meu models de usuario

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['descricao','data_abertura','data_fechamento','solicitante',
                'tecnico_responsavel','equipamento','setor','status','prioridade']
        widgets = {
            'data_abertura': forms.DateInput(attrs={'type': 'date'}),
            'data_fechamento': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tecnico_responsavel'].queryset = Usuario.objects.filter(tipo_usuario='tecnico')
      