from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
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
    total_criticos = Chamado.objects.filter(prioridade='critica').count()

    # Contagem geral
    total_setores = Setor.objects.count()
    total_equipamentos = Equipamento.objects.count()
    total_usuarios = Usuario.objects.count()

    # ================================
    # Dados para o gráfico de linha (últimos 7 dias)
    hoje = timezone.now().date()
    labels_dias = []
    valores_dias = []

    for i in range(6, -1, -1):  # 7 dias (do mais antigo ao mais recente)
        dia = hoje - timedelta(days=i)
        labels_dias.append(dia.strftime("%d/%m"))
        qtd_chamados = Chamado.objects.filter(data_abertura=dia).count()
        valores_dias.append(qtd_chamados)

    # Dados para o gráfico de pizza
    pizza_labels = ['Abertos', 'Em Atendimento', 'Resolvidos', 'Alertas Críticos']
    pizza_valores = [total_abertos, total_em_atendimento, total_resolvidos, total_criticos]
    # ================================

    context = {
        'total_abertos': total_abertos,
        'total_em_atendimento': total_em_atendimento,
        'total_resolvidos': total_resolvidos,
        'total_criticos': total_criticos,
        'total_setores': total_setores,
        'total_equipamentos': total_equipamentos,
        'total_usuarios': total_usuarios,

        # Dados dos gráficos
        'labels_dias': labels_dias,
        'valores_dias': valores_dias,
        'pizza_labels': pizza_labels,
        'pizza_valores': pizza_valores,
    }

    return render(request, 'dashboard.html', context)
