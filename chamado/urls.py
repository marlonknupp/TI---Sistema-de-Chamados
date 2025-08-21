from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_chamado, name='lista_chamado'),
    path('criar/', views.criar_chamado, name='criar_chamado'),
    path('chamado/<int:pk>/', views.ver_chamado, name='ver_chamado'),
    path('chamado/<int:pk>/editar/', views.editar_chamado, name='editar_chamado'),
    path('chamado/<int:pk>/deletar/', views.deletar_chamado, name='deletar_chamado'),
    path('chamado/status/<str:status>/', views.status_chamado, name='status_chamado'),
    
]