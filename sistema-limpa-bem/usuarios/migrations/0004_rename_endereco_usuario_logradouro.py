# Generated by Django 4.1.7 on 2023-02-16 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_usuario_sobrenome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='endereco',
            new_name='logradouro',
        ),
    ]
