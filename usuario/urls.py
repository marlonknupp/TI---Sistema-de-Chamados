from django.urls import path
from .import views

urlpatterns = [
    path('lista/', views.lista_usuario, name='lista_usuario'),
]