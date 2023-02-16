import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.db.models import F, Q, TextField, Value
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


@login_required(login_url='/auth/login/')
def principal(request):
    page = 'Principal'
    return render(request, 'principal.html', {'page': page})

@login_required(login_url='/auth/login/')
@user_passes_test(lambda u: u.is_superuser)
def servicos_page(request):
    if request.method == 'GET':
        page = 'Servicos'
        return render(request, 'servicos.html', {'page': page})

@login_required(login_url='/auth/login/')
@user_passes_test(lambda u: u.is_superuser)
def servicos_data(request):
    servicos = []
    if request.method == 'GET':
        servicos_query = Servico.objects.all()

        for servico in servicos_query:
            servicos.append({'nome': servico.nome, 'valor': servico.valor, 'disp': servico.disponivel, 'id': servico.pk})

        # print(servicos, '\n\n\n')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        dados = json.loads(body_unicode)

        # print('\n\n\n', dados, '\n\n\n')

        Servico(nome=dados['nome'], valor=dados['valor'], disponivel=dados['disp']).save()
    elif request.method == 'PATCH':
        body_unicode = request.body.decode('utf-8')
        dados = json.loads(body_unicode)

        # print('\n\n\n patch aqui', dados, '\n\n\n')

        obj = Servico.objects.get(pk=dados['id'])
        obj.nome = dados['nome']
        obj.valor = dados['valor']
        obj.save()
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        dados = json.loads(body_unicode)

        obj = Servico.objects.get(pk=dados['id'])
        obj.delete()

    return HttpResponse(json.dumps(servicos), content_type='application/json;charset=utf-8')
