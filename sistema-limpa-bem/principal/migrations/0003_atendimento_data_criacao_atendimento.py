# Generated by Django 4.1.7 on 2023-02-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_atendimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='data_criacao_atendimento',
            field=models.DateTimeField(default='2022-12-01'),
            preserve_default=False,
        ),
    ]
