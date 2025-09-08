from django.db import models
from usuario.models import Usuario

class Comentario(models.Model):
    usuario =  models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    mensagem = models.TextField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario}'