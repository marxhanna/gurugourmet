# Generated by Django 5.0.3 on 2024-05-23 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_usuario_cnpj_usuario_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='empresa',
        ),
    ]