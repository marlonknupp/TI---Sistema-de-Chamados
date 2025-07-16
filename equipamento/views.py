from django.shortcuts import render, redirect
from .models import Equipamento
from .forms import EquipamentoForm

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