from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),         # URL da página inicial
    path('perdidos/', views.perdidos, name='perdidos'),  
    path('achados/', views.achados, name='achados'),  
    path('cadastro/', views.cadastrar, name='cadastro'),  # <-- recebe "perdido" ou "achado"
    path('voltar/', views.voltar, name='voltar'),  
    path('cadastro_user/', views.cadastro_user, name='cadastro_user'),  
    path('login/', views.login, name='login'),  
]
