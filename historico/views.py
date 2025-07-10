from django.shortcuts import render
from .models import Historico

def lista_historico(request):
    historicos = Historico.objects.all()
    return render(request, 'historico/lista.html',{'historico': historicos})