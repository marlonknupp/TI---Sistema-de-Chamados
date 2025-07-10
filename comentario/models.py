from django.db import models
from chamado.models import Chamado
from usuario.models import Usuario

class Comentario(models.Model):
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE, null=True, blank=True)
    autor =  models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor}'