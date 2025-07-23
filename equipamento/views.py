from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Equipamento
from .forms import EquipamentoForm

@login_required
def lista_equipamento(request):
    equipamentos = Equipamento.objects.all()
    return render(request,'equipamento/lista.html', {'equipamentos': equipamentos})

def criar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipamento')
    else:
        form = EquipamentoForm()
    return render(request, 'equipamento/criar.html', {'form': form})

def ver_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    return render(request, 'equipamento/ver.html', {'equipamento': equipamento})

def editar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('lista_equipamento')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamento/editar.html', {'form': form})

def deletar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        return redirect('lista_equipamento')
    return render(request, 'equipamento/deletar.html', {'equipamento': equipamento})