from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('login/', views.login, name = 'login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastrar/funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('cadastrar/cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),

    # PEGANDO UM USER, OU TODOS OS USERS
    path('get/usuario/', views.getUsuarios, name='get_usuarios'),
    path('get/usuario/username/<str:username>/', views.getUsuarioByUsername, name='get_usuario_by_username'),
    path('get/usuario/nome/<str:nome>/', views.getUsuarioByNome, name='get_usuario_by_nome'),
    path('get/usuario/email/<str:email>/', views.getUsuarioByEmail, name='get_usuario_by_email'),
    path('get/usuario/telefone/<str:telefone>/', views.getUsuarioByTelefone, name='get_usuario_by_telefone'),
    path('get/usuario/id/<str:id>/', views.getUsuarioById, name='get_usuario_by_id'),

    #   VALIDACOES 
    path('validar/usuario/', views.user_validation, name='validacao_usuario')
    ]