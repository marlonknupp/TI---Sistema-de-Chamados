from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_equipamento, name='lista_equipamento'),
    path('criar/', views.criar_equipamento, name='criar_equipamento'),
]