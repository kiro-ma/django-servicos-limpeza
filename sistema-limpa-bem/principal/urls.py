from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('', views.principal, name = 'principal_principal'),
    path('servicos/', views.servicos_page, name = 'principal_servicos_page'),
    path('servicos/save/', views.servicos_data, name = 'principal_servicos_data'),
    ]