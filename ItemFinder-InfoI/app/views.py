from django.shortcuts import render

# Página inicial
def index(request):
    return render(request, 'app/index.html')

# Página de objetos perdidos
def perdidos(request):
    return render(request, 'app/perdidos.html')

def achados(request):
    return render(request, 'app/achados.html')


def cadastrar(request):
    return render(request, 'app/cadastrar.html')
