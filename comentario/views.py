from django.shortcuts import render
from .models import Comentario

def lista_comentario(request):
    comentarios = Comentario.objects.all()
    return render(request, 'comentario/lista.html', {'comentarios': comentarios})