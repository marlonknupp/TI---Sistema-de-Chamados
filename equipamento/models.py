from django.db import models
from setor.models import Setor

class Equipamento (models.Model):
    nome = models.CharField(max_length=200)
    numero_patrimonio = models.CharField(max_length=20, unique=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, blank=True)

    TIPO_CHOICE = [
        ('notebook','Notebooks'),
        ('monitores','Monitores'),
        ('estabilizadores','Estabilizadores'),
        ('teclados','Teclados'),
        ('mouses','Mouse'),
        ('impressoras','Impressoras'),
        ('switch','Switch'),
    ]

    STATUS_CHOICE = [
        ('ativo','Ativo'),
        ('manutencao','Manutenção'),
        ('descartado','Descartado'),

    ]

    tipo =  models.CharField(max_length=50, choices=TIPO_CHOICE, default='notebook')
    status = models.CharField(max_length=40, choices=STATUS_CHOICE, default='ativo')

    def __str__(self):
        return f'{self.nome} ({self.tipo}, {self.status})'