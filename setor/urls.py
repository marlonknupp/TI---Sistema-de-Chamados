from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_setor, name='lista_setor'),
    path('criar/', views.criar_setor, name='criar_setor'),
    path('setor/<int:pk>/', views.ver_setor, name='ver_setor'),
    path('setor/<int:pk>/editar/', views.editar_setor, name='editar_setor'),
    path('setor/<int:pk>/deletar/', views.deletar_setor, name='deletar_setor'),
]