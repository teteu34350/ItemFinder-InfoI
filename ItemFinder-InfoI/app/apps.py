from django.apps import AppConfig
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
class ItemPerdido(View):
    def get(self,request):
        return render(request,'index.html')
