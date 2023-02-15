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

        print('\n\n', username, senha, '\n\n')

        user = authenticate(username=username, password=senha)
        if user:
            return HttpResponse(json.dumps({'status': 'OK'}), status=200, content_type='application/json;charset=utf-8')
        else:
            return HttpResponse(json.dumps({'status': 'ERROR'}), status=406, content_type='application/json;charset=utf-8')