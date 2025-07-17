from django.shortcuts import render, redirect, get_object_or_404
from .models import Comentario
from .forms import ComentarioForm

def lista_comentario(request):
    comentarios = Comentario.objects.all()
    return render(request, 'comentario/lista.html', {'comentarios': comentarios})


def criar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_comentario')
    else:
        form = ComentarioForm()
    return render(request, 'comentario/criar.html', {'form': form})

def ver_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    return render(request, 'comentario/ver.html', {'comentario': comentario})

def editar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('lista_comentario')
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'comentario/editar.html', {'form': form})

def deletar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    if request.method == 'POST':
        comentario.delete()
        return redirect('lista_comentario')
    return render(request, 'comentario/deletar.html', {'comentario': comentario})

