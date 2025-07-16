from django.shortcuts import render, redirect
from .models import Setor
from .forms import SetorForm

def lista_setor(request):
    setors = Setor.objects.all()
    return render(request, 'setor/lista.html', {'setors': setors})

def criar_setor(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_setor')
    else:
        form = SetorForm()
    return render(request, 'setor/criar.html', {'form': form})