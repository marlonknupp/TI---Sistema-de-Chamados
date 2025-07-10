from django.shortcuts import render
from .models import Usuario

def lista_usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/lista.html', {'usuario': usuarios})