from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.principal, name='principal_principal'),
    path('servicos/', views.servicos_page, name='principal_servicos_page'),
    path('servicos/save/', views.servicos_data, name='principal_servicos_data'),
    path('servicos/cliente/', views.get_servicos_data, name='principal_get_servicos_data'),
    path('agendamento/', views.agendamento, name='principal_agendamento'),
    path('agendamento/save/', views.agendamento_data, name='principal_agendamento'),
    path('agendamento/save/<str:id_cliente>/', views.agendamento_data_by_id, name='principal_agendamento_by_id'),

    path('atendimento/save/', views.atendimento, name="principal_atendimento"),
    path('atendimento/save/<int:id>/', views.atendimento_by_id, name="principal_atendimento_by_id"),
    path('atendimento/save/dia/', views.atendimento_dia, name="principal_atendimento_dia"),
    path('atendimento/save/mes/', views.atendimento_mes, name="principal_atendimento_mes"),

    path('usuarios/', include('usuarios.urls')),
    path('gerenciar-agendamento/', views.gerenciar_agendamento, name='principal_gerenciar_agendamento'),
    path('relatórios/', views.relatorios, name='principal_relatorios'),
]
