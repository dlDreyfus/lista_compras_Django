from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_lista, name='lista'),
    path('editar/<int:pk>/', views.editar_item, name='editar'),
    path('deletar/<int:pk>/', views.deletar_item, name='deletar'),
    path('alternar_status/<int:pk>/', views.alternar_status, name='alternar_status'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
