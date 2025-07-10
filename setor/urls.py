from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_setor, name='lista_setor'),
]