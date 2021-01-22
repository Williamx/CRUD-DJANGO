from django.urls import path

from jornal import views

urlpatterns = [
    path('', views.index, name='index'),
    path('atualizar/', views.atualizar, name='atualizar'),
    path('deletar/', views.deletar, name='deletar'),
    path('inserir/', views.inserir, name='inserir')
]