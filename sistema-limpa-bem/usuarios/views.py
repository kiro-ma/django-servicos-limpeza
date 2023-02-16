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


# def getUsuarios(request):
#     if request.method == 'GET':
#         usuarios = Usuario.objects.all()
#         lista_de_usuarios = []
#         for usuario in usuarios:
#             dados = {
#                 'nome': usuario.first_name,
#                 'userID': usuario.username
#             }
#             lista_de_usuarios.append(dados)

#     return HttpResponse(json.dumps(lista_de_usuarios), content_type='application/json;charset=utf-8')


# def getUsuario(request, username):
#     if request.method == 'GET':
#         query = Usuario.objects.filter(username=username).get()
#         userDict = {
#             'nome': query.first_name,
#             'username': query.username,
#             'cpf': query.cpf,
#             'funcao': query.funcao,
#             'email': query.email,
#             'dataAdmissao': query.dataAdmissao,
#             'assinaDoc': query.snassina,
#             'avisaEstoque': query.bitAvisaEstoqueMinimo,
#             'avisaTeto': query.bitAvisaTetoConstitucional,
#             'is_staff': query.is_staff,
#             'dataNascimento': query.dataNascimento
#         }
#     return HttpResponse(json.dumps(userDict, indent=4, sort_keys=True, default=str), content_type='application/json;charset=utf-8')

@login_required(login_url='/auth/login/')
@user_passes_test(lambda u: u.is_superuser)
def cadastrar_funcionario(request):
    if request.method == 'GET':
        page = "Cadastro de funcionarios"
        return render(request, 'cadastro_funcionarios.html', {'page': page})
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmarSenha = request.POST.get('senha2')

        tipo_user = request.POST.get('tipo_user')
        nome = request.POST.get('nome')

        if senha != confirmarSenha:
            return HttpResponse('Senha incompatível.')

        if len(senha) < 4:
            return HttpResponse('Senha muito curta, mínimo de quatro caracteres.')

        nome = request.POST.get('nome')

        user = Usuario.objects.filter(username=username).first()

        if user:
            user.first_name = nome
            user.set_password(senha)
            user.email = email
            user.tipo_user = tipo_user
            user.save()
            return render(request, 'cadastro_funcionarios.html', {'editado': user.username})

    
        # \/ Pra ser ADM um usuário teria is_staff=True
        user = Usuario.objects.create_user(username=username, email=email, password=senha)

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
