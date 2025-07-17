from django.shortcuts import render, redirect, get_object_or_404
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

def ver_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'usuario/ver.html', {'usuario': usuario})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuario')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario/editar.html', {'form': form})

def deletar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuario')
    return render(request, 'usuario/deletar.html', {'usuario': usuario})