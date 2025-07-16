from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome','email','senha','tipo_usuario','setor']
        widgets = {
            'senha': forms.PasswordInput(attrs={'placeholder': 'Digite a senha'}),
 
        }