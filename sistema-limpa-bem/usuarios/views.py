import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from .models import Usuario
from django.contrib.auth.models import Group

def is_gerente(user):
    return user.groups.filter(name='Gerentes').exists()


def is_atendente(user):
    return user.groups.filter(name='Atendentes').exists()

def is_gerente_or_atendente(user):
    return (user.groups.filter(name='Gerentes').exists() or user.groups.filter(name='Atendentes').exists())


@user_passes_test(is_gerente_or_atendente)
def getUsuarios(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        lista_de_usuarios = []
        for usuario in usuarios:
            dados = {
                'first_name': usuario.first_name,
                'username': usuario.username
            }
            lista_de_usuarios.append(dados)

    return HttpResponse(json.dumps(lista_de_usuarios), content_type='application/json;charset=utf-8')


@user_passes_test(is_gerente_or_atendente)
def getUsuarioByUsername(request, username):
    if request.method == 'GET':
        query = Usuario.objects.filter(username=username).get()
        userDict = {
            'is_superuser': query.is_superuser,
            'username': query.username,
            'first_name': query.first_name,
            'last_name': query.last_name,
            'email': query.email,
            'cidade' : query.cidade,
            'logradouro' : query.logradouro,
            'estado' : query.estado,
            'numero' : query.numero,
            'telefone' : query.telefone,
            'id' : query.pk
        }
    return HttpResponse(json.dumps(userDict, indent=4, sort_keys=True, default=str), content_type='application/json;charset=utf-8')


@user_passes_test(is_gerente_or_atendente)
def getUsuarioByNome(request, nome):
    if request.method == 'GET':
        query = Usuario.objects.filter(first_name=nome).get()
        userDict = {
            'is_superuser': query.is_superuser,
            'username': query.username,
            'first_name': query.first_name,
            'last_name': query.last_name,
            'email': query.email,
            'cidade' : query.cidade,
            'logradouro' : query.logradouro,
            'estado' : query.estado,
            'numero' : query.numero,
            'telefone' : query.telefone,
            'id' : query.pk
        }
    return HttpResponse(json.dumps(userDict, indent=4, sort_keys=True, default=str), content_type='application/json;charset=utf-8')

@user_passes_test(is_gerente_or_atendente)
def getUsuarioByEmail(request, email):
    if request.method == 'GET':
        query = Usuario.objects.filter(email=email).get()
        userDict = {
            'is_superuser': query.is_superuser,
            'username': query.username,
            'first_name': query.first_name,
            'last_name': query.last_name,
            'email': query.email,
            'cidade' : query.cidade,
            'logradouro' : query.logradouro,
            'estado' : query.estado,
            'numero' : query.numero,
            'telefone' : query.telefone,
            'id' : query.pk
        }
    return HttpResponse(json.dumps(userDict, indent=4, sort_keys=True, default=str), content_type='application/json;charset=utf-8')

@user_passes_test(is_gerente_or_atendente)
def getUsuarioByTelefone(request, telefone):
    if request.method == 'GET':
        query = Usuario.objects.filter(telefone=telefone).get()
        userDict = {
            'is_superuser': query.is_superuser,
            'username': query.username,
            'first_name': query.first_name,
            'last_name': query.last_name,
            'email': query.email,
            'cidade' : query.cidade,
            'logradouro' : query.logradouro,
            'estado' : query.estado,
            'numero' : query.numero,
            'telefone' : query.telefone,
            'id' : query.pk
        }
    return HttpResponse(json.dumps(userDict, indent=4, sort_keys=True, default=str), content_type='application/json;charset=utf-8')


@login_required(login_url='/auth/login/')
@user_passes_test(is_gerente)
def cadastrar_funcionario(request):
    if request.method == 'GET':
        page = "Cadastro de funcionarios"
        return render(request, 'cadastro_funcionarios.html', {'page': page})
    else:
        username = request.POST.get('username')
        # só é usado pra atribuir um grupo
        tipo_user = request.POST.get('tipo_user')
        senha = request.POST.get('senha')
        confirmarSenha = request.POST.get('senha2')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        dict_tipo_user = {
            '0': 'Clientes',
            '1': 'Helpers',
            '2': 'Atendentes',
            '3': 'Gerentes'
        }

        if senha != confirmarSenha:
            return HttpResponse('Senha incompatível.')

        if len(senha) < 4:
            return HttpResponse('Senha muito curta, mínimo de quatro caracteres.')

        user = Usuario.objects.filter(username=username).first()

        if user:
            user.first_name = nome
            user.set_password(senha)
            user.email = email
            user.tipo_user = tipo_user
            user.save()
            return render(request, 'cadastro_funcionarios.html', {'editado': user.username})

        # \/ Pra ser ADM um usuário teria is_staff=True
        user = Usuario.objects.create_user(username=username, email=email, password=senha, telefone=telefone, first_name=nome,
                                           last_name=sobrenome, logradouro=logradouro, numero=numero, cidade=cidade, estado=estado, tipo_user=tipo_user)

        group = Group.objects.get(name=dict_tipo_user[f"{tipo_user}"])
        user.groups.add(group)

        user.save()
        return render(request, 'cadastro_funcionarios.html', {'editado': False})


def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username


def logout_view(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        return render(request, 'login.html', {'login_error': False})

# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'login_error': False})
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponseRedirect('/principal/')
        else:
            return HttpResponse(status=406)


def user_validation(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        request_body = json.loads(body_unicode)

        username = request_body['username']
        senha = request_body['senha']

        user = authenticate(username=username, password=senha)
        if user:
            return HttpResponse(json.dumps({'status': 'OK'}), status=200, content_type='application/json;charset=utf-8')
        else:
            return HttpResponse(json.dumps({'status': 'ERROR'}), status=406, content_type='application/json;charset=utf-8')
