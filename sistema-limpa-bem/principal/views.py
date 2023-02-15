import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.db.models import F, Q, TextField, Value
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/login/')
def principal(request):
    page = 'Principal'
    return render(request, 'principal.html', {'page': page})