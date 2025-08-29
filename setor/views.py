from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Setor
from .forms import SetorForm

@login_required
def lista_setor(request):
    setors = Setor.objects.all()
    return render(request, 'setor/lista.html', {'setors': setors})

def criar_setor(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_setor')
    else:
        form = SetorForm()
    return render(request, 'setor/criar.html', {'form': form})

def ver_setor(request, pk):
    setor = get_object_or_404(Setor, pk=pk)
    return render(request, 'setor/ver.html', {'setor': setor})

def editar_setor(request, pk):
    setor = get_object_or_404(Setor, pk=pk)
    if request.method == 'POST':
        form = SetorForm(request.POST, instance=setor)
        if form.is_valid():
            form.save()
            return redirect('lista_setor')
    else:
        form = SetorForm(instance=setor)
    return render(request, 'setor/editar.html', {'form': form})

def deletar_setor(request, pk):
    setor = get_object_or_404(Setor, pk=pk)
    if request.method == 'POST':
        setor.delete()
        return redirect('lista_setor')
    return render(request, 'setor/deletar.html', {'setor': setor})