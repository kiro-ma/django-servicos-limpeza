# Generated by Django 4.1.7 on 2023-02-16 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('valor', models.FloatField()),
                ('disponivel', models.BooleanField()),
            ],
        ),
    ]
