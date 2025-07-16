from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def lista_usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/lista.html', {'usuarios': usuarios})

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuario')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/criar.html', {'form': form})