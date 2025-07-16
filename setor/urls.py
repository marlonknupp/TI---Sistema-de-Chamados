from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_setor, name='lista_setor'),
    path('criar/', views.criar_setor, name='criar_setor'),
]