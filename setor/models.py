from django.db import models

class Setor(models.Model):
    nome = models.CharField(max_length=50)
    andar = models.CharField(max_length=40)

    def __str__(self):
        return self.nome