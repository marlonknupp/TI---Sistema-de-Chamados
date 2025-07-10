from django.shortcuts import render
from .models import Setor

def lista_setor(request):
    setors = Setor.objects.all()
    return render(request, 'setor/lista.html', {'setors': setors})