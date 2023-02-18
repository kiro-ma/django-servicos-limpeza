from django.db import models

# Create your models here.


class Servico(models.Model):
    nome = models.CharField(max_length=80)
    valor = models.FloatField()
    disponivel = models.BooleanField()


class Atendimento(models.Model):
    atendente = models.IntegerField()
    helper = models.IntegerField()
    cliente = models.IntegerField()
    servico = models.IntegerField()
    data_hora = models.DateTimeField()
    preco = models.FloatField()
    situacao = models.IntegerField()
    pagamento = models.IntegerField()
    nome_cliente = models.CharField(max_length=50)
    telefone_cliente = models.CharField(max_length=50)
    logradouro_cliente = models.CharField(max_length=50)
    numero_casa_cliente = models.CharField(max_length=50)
    cidade_cliente = models.CharField(max_length=50)
    estado_cliente = models.CharField(max_length=50)
    data_criacao_atendimento = models.DateTimeField()


class Agendamento(models.Model):
    id_cliente = models.IntegerField()
    servico = models.IntegerField()
    data_reservada = models.DateTimeField()
    data_de_criacao = models.DateTimeField()
    valor = models.FloatField()
    