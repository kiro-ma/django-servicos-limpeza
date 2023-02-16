from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('login/', views.login, name = 'login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastrar/funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    #   VALIDACOES 
    path('validar/usuario/', views.user_validation, name='validacao_usuario')
    ]