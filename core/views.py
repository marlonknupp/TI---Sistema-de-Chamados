from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chamado.models import Chamado
from setor.models import Setor
from equipamento.models import Equipamento
from usuario.models import Usuario

@login_required
def dashboard(request):
    # Contagem de chamados
    total_abertos = Chamado.objects.filter(status='aberto').count()
    total_em_atendimento = Chamado.objects.filter(status='em_atendimento').count()
    total_resolvidos = Chamado.objects.filter(status='resolvido').count()
    total_cancelados = Chamado.objects.filter(status='cancelado').count()
    total_criticos = Chamado.objects.filter(prioridade='critica').count()

    # Contagem geral
    total_setores = Setor.objects.count()
    total_equipamentos = Equipamento.objects.count()
    total_usuarios = Usuario.objects.count()

    context = {
        'total_abertos': total_abertos,
        'total_em_atendimento': total_em_atendimento,
        'total_resolvidos': total_resolvidos,
        'total_cancelados': total_cancelados,
        'total_criticos': total_criticos,
        'total_setores': total_setores,
        'total_equipamentos': total_equipamentos,
        'total_usuarios': total_usuarios,
    }

    return render(request, 'dashboard.html', context)
