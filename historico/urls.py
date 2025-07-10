from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_historico, name='lista_historico'),
]