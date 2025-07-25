# Generated by Django 5.2.3 on 2025-07-02 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chamado', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_anterior', models.CharField(max_length=100)),
                ('status_novo', models.CharField(max_length=100)),
                ('data_alteracao', models.DateTimeField(auto_now_add=True)),
                ('alterado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario')),
                ('chamado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chamado.chamado')),
            ],
        ),
    ]
