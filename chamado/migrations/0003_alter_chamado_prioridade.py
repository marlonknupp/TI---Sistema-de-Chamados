# Generated by Django 5.2.3 on 2025-07-23 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0002_remove_chamado_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='prioridade',
            field=models.CharField(choices=[('baixa', 'Baixa'), ('media', 'Media'), ('alta', 'Alta'), ('critica', 'Critica')], default='media', max_length=20),
        ),
    ]
