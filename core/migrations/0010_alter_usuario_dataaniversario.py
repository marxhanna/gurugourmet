# Generated by Django 5.0.3 on 2024-06-11 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_usuario_dataaniversario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='dataAniversario',
            field=models.DateTimeField(max_length=128, null=True),
        ),
    ]
