from django import forms
from .models import Usuario

class Usuario(forms.modelForm):
    class Meta:
        model = Usuario
        fields = ['nome','email','senha','tipo_usuario','setor']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # aparece o caléndario 
        }