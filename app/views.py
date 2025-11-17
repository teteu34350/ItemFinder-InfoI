from django.shortcuts import render
from django.shortcuts import redirect  # <-- Adicione essa linha
from .models import ItemPerdido, ItemAchado
from .forms import ItemPerdidoForm, ItemAchadoForm
from django.contrib.auth.decorators import login_required

def perfil(request):
    # Renderiza a página do perfil do usuário
    return render(request, 'app/perfil.html')

def meus_cadastros(request):
    # Renderiza a página de cadastros do usuário
    return render(request, 'app/meus_cadastros.html')

# Página inicial
def index(request):
    return render(request, 'app/index.html')

@login_required
def meus_cadastros(request):
    return render(request, 'app/meus_cadastros.html')
@login_required
def perfil(request):
    return render(request, 'app/perfil.html', {"usuario": request.user})


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

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Perfil

def cadastro(request):
    if request.method == 'POST':
        tipo = request.POST.get('userType')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma = request.POST.get('confirmaSenha')

        # Validações
        if senha != confirma:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'cadastro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Esse e-mail já está cadastrado.")
            return render(request, 'app/cadastro.html')

        # Criar usuário
        user = User.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome
        )

        # Criar perfil
        Perfil.objects.create(
            user=user,
            tipo=tipo
        )

        messages.success(request, "Conta criada com sucesso! Faça login.")
        return redirect('login')

    return render(request, 'app/cadastro.html')
