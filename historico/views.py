from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Historico
from .forms import HistoricoForm

@login_required
def lista_historico(request):
    historicos = Historico.objects.all()
    return render(request, 'historico/lista.html',{'historico': historicos})

