from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('login/', views.login, name = 'login'),
    path('logout/', views.logout_view, name='logout'),
    #   VALIDACOES 
    path('validar/usuario/', views.user_validation, name='validacao_usuario')
    ]