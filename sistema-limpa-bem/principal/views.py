import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.db.models import F, Q, TextField, Value
from django.contrib.auth.decorators import login_required, user_passes_test
from usuarios import models as usuarios_models
# Create your views here.


def is_gerente(user):
    return user.groups.filter(name='Gerentes').exists()


def is_atendente(user):
    return user.groups.filter(name='Atendentes').exists()


def is_gerente_or_atendente(user):
    return (user.groups.filter(name='Gerentes').exists() or user.groups.filter(name='Atendentes').exists())


@login_required(login_url='/auth/login/')
def principal(request):
    page = 'Principal'
    return render(request, 'principal.html', {'page': page})


@login_required(login_url='/auth/login/')
def agendamento(request):
    page = 'Agendamento'
    return render(request, 'agendamento.html', {'page': page})

@login_required(login_url='/auth/login/')
def agendamento_data_by_id(request, id_cliente):
    agendamentos = []
    if request.method == 'GET':
        agendamentos_query = Agendamento.objects.filter(id_cliente=id_cliente)

        for agendamento in agendamentos_query:
            agendamentos.append({'id_cliente': agendamento.id_cliente, 'servico': agendamento.servico, 'id': agendamento.pk,
                                'data_reservada': agendamento.data_reservada, 'data_de_criacao': agendamento.data_de_criacao, 'valor': agendamento.valor})
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        dados = json.loads(body_unicode)

        Agendamento(id_cliente=dados['id_cliente'], servico=dados['servico'],
                    data_reservada=dados['data_reservada'], data_de_criacao=dados['data_de_criacao'], valor=dados['valor']).save()
    if request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        dados = json.loads(body_unicode)
        Agendamento.objects.get(pk=dados['id'], id_cliente=id_cliente).delete()
    return HttpResponse(json.dumps(agendamentos, indent=4, sort_keys=True, default=str), content_type='application/json;charset=utf-8')


@login_required(login_url='/auth/login/')
def agendamento_data(request):
    agendamentos = []
    if request.method == 'GET':
        agendamentos_query = Agendamento.objects.all()

        for agendamento in agendamentos_query:
            agendamentos.append({'id_cliente': agendamento.id_cliente, 'servico': agendamento.servico, 'id': agendamento.pk,
                                'data_reservada': agendamento.data_reservada, 'data_de_criacao': agendamento.data_de_criacao, 'valor': agendamento.valor})
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        dados = json.loads(body_unicode)

        Agendamento(id_cliente=dados['id_cliente'], servico=dados['servico'],
                    data_reservada=dados['data_reservada'], data_de_criacao=dados['data_de_criacao'], valor=dados['valor']).save()
    if request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        dados = json.loads(body_unicode)
        print('\n\n\n dados', dados, '\n\n\n')
        Agendamento.objects.get(pk=dados['id']).delete()
    return HttpResponse(json.dumps(agendamentos, indent=4, sort_keys=True, default=str), content_type='application/json;charset=utf-8')


@login_required(login_url='/auth/login/')
@user_passes_test(is_gerente)
def servicos_page(request):
    if request.method == 'GET':
        page = 'Servicos'
        return render(request, 'servicos.html', {'page': page})


@login_required(login_url='/auth/login/')
def get_servicos_data(request):
    servicos = []
    if request.method == 'GET':
        servicos_query = Servico.objects.all()

        for servico in servicos_query:
            servicos.append({'nome': servico.nome, 'valor': servico.valor,
                            'disp': servico.disponivel, 'id': servico.pk})
    return HttpResponse(json.dumps(servicos), content_type='application/json;charset=utf-8')


@login_required(login_url='/auth/login/')
@user_passes_test(is_gerente_or_atendente)
def servicos_data(request):
    servicos = []
    if request.method == 'GET':
        servicos_query = Servico.objects.all()

        for servico in servicos_query:
            servicos.append({'nome': servico.nome, 'valor': servico.valor,
                            'disp': servico.disponivel, 'id': servico.pk})

        # print(servicos, '\n\n\n')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        dados = json.loads(body_unicode)

        # print('\n\n\n', dados, '\n\n\n')

        Servico(nome=dados['nome'], valor=dados['valor'],
                disponivel=dados['disp']).save()
    elif request.method == 'PATCH':
        body_unicode = request.body.decode('utf-8')
        dados = json.loads(body_unicode)

        # print('\n\n\n patch aqui', dados, '\n\n\n')

        obj = Servico.objects.get(pk=dados['id'])
        obj.nome = dados['nome']
        obj.valor = dados['valor']
        obj.disponivel = dados['disp']
        obj.save()
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        dados = json.loads(body_unicode)

        obj = Servico.objects.get(pk=dados['id'])
        obj.delete()

    return HttpResponse(json.dumps(servicos), content_type='application/json;charset=utf-8')


@login_required(login_url='/auth/login/')
@user_passes_test(is_gerente_or_atendente)
def atendimento(request):
    atendimentos = []
    if request.method == 'GET':
        atendimentos_query = Atendimento.objects.filter(situacao=0)
        for atendimento in atendimentos_query:
            atendimentos.append({'atendente': atendimento.atendente,
                                'helper': atendimento.helper,
                                 'cliente': atendimento.cliente,
                                 'servico': atendimento.servico,
                                 'data_hora': atendimento.data_hora,
                                 'preco': atendimento.preco,
                                 'situacao': atendimento.situacao,
                                 'pagamento': atendimento.pagamento,
                                 'nome_cliente': atendimento.nome_cliente,
                                 'telefone_cliente': atendimento.telefone_cliente,
                                 'logradouro_cliente': atendimento.logradouro_cliente,
                                 'numero_casa_cliente': atendimento.numero_casa_cliente,
                                 'cidade_cliente': atendimento.cidade_cliente,
                                 'data_criacao_atendimento': atendimento.data_criacao_atendimento,
                                 'estado_cliente': atendimento.estado_cliente,
                                 'id': atendimento.pk})

    elif request.method == 'PATCH':
        body_unicode = request.body.decode('utf-8')
        dados = json.loads(body_unicode)
        obj = Atendimento.objects.get(pk=dados['id'])

        obj.atendente = dados['atendente']
        obj.helper = dados['helper']
        obj.cliente = dados['cliente']
        obj.servico = dados['servico']
        obj.data_hora = dados['data_hora']
        obj.preco = dados['preco']
        obj.situacao = dados['situacao']
        obj.pagamento = dados['pagamento']
        obj.nome_cliente = dados['nome_cliente']
        obj.telefone_cliente = dados['telefone_cliente']
        obj.logradouro_cliente = dados['logradouro_cliente']
        obj.numero_casa_cliente = dados['numero_casa_cliente']
        obj.cidade_cliente = dados['cidade_cliente']
        obj.data_criacao_atendimento = dados['data_criacao_atendimento']
        obj.estado_cliente = dados['estado_cliente']

        obj.save()

    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        dados = json.loads(body_unicode)

        Atendimento(atendente=dados['atendente'],
                    helper=dados['helper'],
                    cliente=dados['cliente'],
                    servico=dados['servico'],
                    data_hora=dados['data_hora'],
                    preco=dados['preco'],
                    situacao=dados['situacao'],
                    pagamento=dados['pagamento'],
                    nome_cliente=dados['nome_cliente'],
                    telefone_cliente=dados['telefone_cliente'],
                    logradouro_cliente=dados['logradouro_cliente'],
                    numero_casa_cliente=dados['numero_casa_cliente'],
                    cidade_cliente=dados['cidade_cliente'],
                    data_criacao_atendimento=dados['data_criacao_atendimento'],
                    estado_cliente=dados['estado_cliente']).save()

    return HttpResponse(json.dumps(atendimentos, indent=4, sort_keys=True, default=str), content_type='application/json;charset=utf-8')


@login_required(login_url='/auth/login/')
@user_passes_test(is_gerente_or_atendente)
def atendimento_by_id(request, id):
    atendimentos = []
    if request.method == 'GET':
        atendimentos_query = Atendimento.objects.filter(pk=id)
        for atendimento in atendimentos_query:
            atendimentos.append({'atendente': atendimento.atendente,
                                'helper': atendimento.helper,
                                 'cliente': atendimento.cliente,
                                 'servico': atendimento.servico,
                                 'data_hora': atendimento.data_hora,
                                 'preco': atendimento.preco,
                                 'situacao': atendimento.situacao,
                                 'pagamento': atendimento.pagamento,
                                 'nome_cliente': atendimento.nome_cliente,
                                 'telefone_cliente': atendimento.telefone_cliente,
                                 'logradouro_cliente': atendimento.logradouro_cliente,
                                 'numero_casa_cliente': atendimento.numero_casa_cliente,
                                 'cidade_cliente': atendimento.cidade_cliente,
                                 'estado_cliente': atendimento.estado_cliente,
                                 'data_criacao_atendimento': atendimento.data_criacao_atendimento,
                                 'id': atendimento.pk})

    return HttpResponse(json.dumps(atendimentos, indent=4, sort_keys=True, default=str), content_type='application/json;charset=utf-8')
