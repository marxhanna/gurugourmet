# Generated by Django 5.0.3 on 2024-05-24 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_merge_20240524_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cnpj',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='dataDescobrimentoBrasil',
        ),
    ]
