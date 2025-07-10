from django.shortcuts import render
from .models import Chamado

def lista_chamado(request):
    chamados = Chamado.objects.all()
    return render (request, 'chamado/lista.html', {'chamados': chamados})