from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .import views

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 

    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='home'),
    path('', views.dashboard, name='home'),
    path('chamado/', include('chamado.urls')),
    path('comentario/', include('comentario.urls')),
    path('equipamento/', include('equipamento.urls')),
    path('historico/', include('historico.urls')),
    path('setor/', include('setor.urls')),
    path('usuario/', include('usuario.urls')),
]
