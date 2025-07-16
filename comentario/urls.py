from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_comentario, name='lista_comentario'),
    path('criar/', views.criar_comentario, name='criar_comentario'),
    ]