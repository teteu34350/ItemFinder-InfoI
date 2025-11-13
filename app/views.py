from django.shortcuts import render
from django.shortcuts import redirect  # <-- Adicione essa linha
from .models import ItemPerdido, ItemAchado
from .forms import ItemPerdidoForm, ItemAchadoForm
def perfil(request):
    # Renderiza a página do perfil do usuário
    return render(request, 'app/perfil.html')

def meus_cadastros(request):
    # Renderiza a página de cadastros do usuário
    return render(request, 'app/meus_cadastros.html')

# Página inicial
def index(request):
    return render(request, 'app/index.html')

# Página de objetos perdidos
# app/views.py
from django.shortcuts import render
from .models import ItemPerdido

def perdidos(request):
    itens = ItemPerdido.objects.all()
    return render(request, 'app/perdidos.html', {'itens': itens})



def achados(request):
    itens = ItemAchado.objects.all().order_by('-id')  
    return render(request, 'app/achados.html', {'itens': itens})

from django.shortcuts import render, redirect
from .forms import ItemPerdidoForm, ItemAchadoForm

def cadastrar(request):
    if request.method == 'POST':
        tipo = request.POST.get('formType')  # perdido ou encontrado
        nome = request.POST.get('nome')
        desc = request.POST.get('descricao')
        categoria = request.POST.get('categoria')
        local = request.POST.get('local')
        data = request.POST.get('data')
        foto = request.FILES.get('foto')

        if tipo == 'encontrado':
            ItemAchado.objects.create(
                nome=nome,
                desc=desc,
                categoria=categoria,
                local=local,
                data=data,
                foto=foto
            )
        else:
            ItemPerdido.objects.create(
                nome=nome,
                desc=desc,
                categoria=categoria,
                local=local,
                data=data,
                foto=foto
            )

        return redirect('index')  # volta pra tela inicial

    return render(request, 'app/cadastro.html')


def voltar(request):
    return render(request, 'app/index.html')

def cadastro_user(request):
    return render(request, 'app/cadastro_user.html')
def login(request):
    return render(request, 'app/login.html')

