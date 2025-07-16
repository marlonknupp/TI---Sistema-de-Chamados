from django.shortcuts import render, redirect
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