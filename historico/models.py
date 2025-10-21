from django.db import models
from chamado.models import Chamado
from usuario.models import Usuario

class Historico(models.Model):
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE, null=True, blank=True)
    descricao = models.CharField(max_length=100)
    alterado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    data_alteracao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.chamado
