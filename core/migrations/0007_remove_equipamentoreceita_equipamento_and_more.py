# Generated by Django 5.0.3 on 2024-04-17 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_receita_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipamentoreceita',
            name='equipamento',
        ),
        migrations.RemoveField(
            model_name='equipamentoreceita',
            name='receita',
        ),
        migrations.DeleteModel(
            name='Equipamento',
        ),
        migrations.DeleteModel(
            name='EquipamentoReceita',
        ),
    ]
