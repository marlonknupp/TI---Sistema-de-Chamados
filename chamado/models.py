from django.db import models
from usuario.models import Usuario
from equipamento.models import Equipamento
from setor.models import Setor


class Chamado (models.Model):
    descricao = models.TextField()
    data_abertura = models.DateField(null=True, blank=True)
    data_fechamento = models.DateField (null=True, blank=True)
    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='chamados_solicitados', null=True, blank=True)
    tecnico_responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='chamados_recebidos', null=True, blank=True)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, null=True, blank=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, blank=True)

    STATUS_CHOICE = [
        ('aberto','Aberto'),
        ('em_atendimento','Em Atendimento'),
        ('resolvido','Resolvido'),
        ('cancelado','Cancelado'),

    ]
    PRIORIDADE_CHOICE = [
        ('baixa','Baixa'),
        ('media','Media'),
        ('alta','Alta'),
        ('critica','Critica'),
    ]

    status =  models.CharField(max_length=20, choices=STATUS_CHOICE, default='aberto')
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE_CHOICE, default='media')

    def __str__(self):
        return f' {self.solicitante}'