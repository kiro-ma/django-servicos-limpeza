# Generated by Django 4.1.7 on 2023-02-16 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_rename_endereco_usuario_logradouro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='complemento',
        ),
    ]
