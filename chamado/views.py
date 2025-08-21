from django.shortcuts import render, redirect
from .models import Chamado
from .forms import ChamadoForm
from historico.models import Historico
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def lista_chamado(request):
    chamados = Chamado.objects.all()
    return render (request, 'chamado/lista.html', {'chamados': chamados})

@login_required
def criar_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_chamado')
    else:
        form = ChamadoForm()
    return render(request, 'chamado/criar.html', {'form': form})

@login_required    
def ver_chamado(request, pk):
    chamado = get_object_or_404(Chamado, pk=pk)
    return render(request, 'chamado/ver.html', {'chamado': chamado})

@login_required
def editar_chamado(request, pk):
    chamado = get_object_or_404(Chamado, pk=pk)
    if request.method == 'POST':
        form = ChamadoForm(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
            return redirect('lista_chamado')
    else:
        form = ChamadoForm(instance=chamado)
    return render(request, 'chamado/editar.html', {'form': form})


@login_required
def deletar_chamado(request, pk):
    chamado = get_object_or_404(Chamado, pk=pk)
    if request.method == 'POST':
        chamado.delete()
        return redirect('lista_chamado')
    return render(request, 'chamado/deletar.html', {'chamado': chamado})

def status_chamado(request, status):
     chamados = Chamado.objects.filter(status=status)
     return render(request, 'chamado/lista.html', {'chamados': chamados, 'status': status})     # retorna somente os chamados em status especificos