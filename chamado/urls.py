from django.urls import path
from .import views

urlpatterns = [
    path('lista/', views.lista_chamado, name='lista_chamado'),
]