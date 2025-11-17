from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.cadastro_user, name='index'),
    path('index/', views.index, name='home'),

    path('perdidos/', views.perdidos, name='perdidos'),
    path('achados/', views.achados, name='achados'),

    path('cadastro_item/', views.cadastrar_item, name='cadastro_item'),
    path('voltar/', views.voltar, name='voltar'),

    path('cadastro_user/', views.cadastro_user, name='cadastro_user'),
    path('registrar/', views.cadastro_user, name='cadastrar_usuario'),

    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('perfil/', views.perfil, name='perfil'),
    path('meus_cadastros/', views.meus_cadastros, name='meus_cadastros'),
]
