from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    TIPO_USUARIO_CHOICES = [
        ('admin', 'Administrador'),
        ('tecnico', 'Técnico'),
        ('funcionario', 'Funcionário'),
    ]

    SETOR_CHOICES = [
        ('financeiro', 'Financeiro'),
        ('ti', 'TI'),
        ('rh', 'Recursos Humanos'),
        ('compras', 'Compras'),
        ('presidade', 'Presidente'),
        ('vice-presidente', 'Vice Precidente'),
        ('ouvidoria', 'Ouvidoria'),
    ]
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
    setor = models.CharField(max_length=20, choices=SETOR_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.nome