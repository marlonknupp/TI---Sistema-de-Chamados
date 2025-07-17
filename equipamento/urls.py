from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_equipamento, name='lista_equipamento'),
    path('criar/', views.criar_equipamento, name='criar_equipamento'),
    path('equipamento/<int:pk>/', views.ver_equipamento, name='ver_equipamento'),
    path('equipamento/<int:pk>/editar/', views.editar_equipamento, name='editar_equipamento'),
    path('equipamento/<int:pk>/deletar/', views.deletar_equipamento, name='deletar_equipamento'),



]