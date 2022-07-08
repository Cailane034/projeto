from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('detalhar/<int:agendamentos_id>/', views.detalhar, name='detalhar'),
    
    path('criar/', views.criar, name='criar'),

    path('editar/<int:agendamentos_id>/', views.editar, name='editar'),

    path('excluir/<int:agendamentos_id>/', views.excluir, name='excluir'),
    
]