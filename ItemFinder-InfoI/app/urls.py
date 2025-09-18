from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),         # URL da página inicial
    path('perdidos/', views.perdidos, name='perdidos'),  # URL da página de objetos perdidos
    path('achados/', views.achados, name='achados'),  # URL da página de objetos perdidos
    path('cadastro/', views.cadastrar, name='cadastrar'),  # <-- função, não módulo

]
