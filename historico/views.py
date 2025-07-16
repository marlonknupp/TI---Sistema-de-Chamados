from django.shortcuts import render, redirect
from .models import Historico
from .forms import HistoricoForm

def lista_historico(request):
    historicos = Historico.objects.all()
    return render(request, 'historico/lista.html',{'historico': historicos})

