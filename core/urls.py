from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.dashboard, name='home'),
    path('chamado/', include('chamado.urls')),
    path('comentario/', include('comentario.urls')),
    path('equipamento/', include('equipamento.urls')),
    path('historico/', include('historico.urls')),
    path('setor/', include('setor.urls')),
    path('usuario/', include('usuario.urls')),
]
