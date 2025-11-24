from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import login_user
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),  # Página inicial REAL
    path('index/', views.index, name='home'),  # opcional, pode até remover

    path('perdidos/', views.perdidos, name='perdidos'),
    path('achados/', views.achados, name='achados'),

    path('cadastro_item/', views.cadastrar_item, name='cadastro_item'),
    path('voltar/', views.voltar, name='voltar'),

    path('cadastro_user/', views.cadastro_user, name='cadastro_user'),
    path('registrar/', views.cadastro_user, name='cadastrar_usuario'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('login/', login_user, name='login'),


    path('perfil/', views.perfil, name='perfil'),
    path('meus_cadastros/', views.meus_cadastros, name='meus_cadastros'),


    path('deletar_conta/', views.deletar_conta, name='deletar_conta'),

   
    path('meus_cadastros/', views.meus_cadastros, name='meus_cadastros'),
    path('marcar_encontrado/<int:item_id>/', views.marcar_encontrado, name='marcar_encontrado'),
    path('marcar_devolvido/<int:item_id>/', views.marcar_devolvido, name='marcar_devolvido'),
    path('deletar_item/<int:item_id>/', views.deletar_item, name='deletar_item'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)