from django.shortcuts import render, redirect
from .models import Chamado
from .forms import ChamadoForm

def lista_chamado(request):
    chamados = Chamado.objects.all()
    return render (request, 'chamado/lista.html', {'chamados': chamados})

def criar_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_chamado')
    else:
        form = ChamadoForm()
    return render(request, 'chamado/criar.html', {'form': form})