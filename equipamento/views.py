from django.shortcuts import render
from .models import Equipamento

def lista_equipamento(request):
    equipamentos = Equipamento.objects.all()
    return render(request,'equipamento/lista.html', {'equipamentos': equipamentos})