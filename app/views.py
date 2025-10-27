from django.shortcuts import render
from django.shortcuts import redirect  # <-- Adicione essa linha


# Página inicial
def index(request):
    return render(request, 'app/index.html')

# Página de objetos perdidos
def perdidos(request):
    return render(request, 'app/perdidos.html')

def achados(request):
    return render(request, 'app/achados.html')

def cadastrar(request):  # <-- adicionar "tipo" aqui
    return render(request, 'app/cadastro.html')

def voltar(request):
    return render(request, 'app/index.html')

def cadastro_user(request):
    return render(request, 'app/cadastro_user.html')
def login(request):
    return render(request, 'app/login.html')

