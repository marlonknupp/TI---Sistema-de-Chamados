from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_comentario, name='lista_comentario'),
    path('criar/', views.criar_comentario, name='criar_comentario'),
    path('comentario/<int:pk>', views.ver_comentario, name='ver_comentario'),
    path('comentario/<int:pk>/editar', views.editar_comentario, name='editar_comentario'),
    path('comentario/<int:pk>/deletar', views.deletar_comentario, name='deletar_comentario'),
    ]