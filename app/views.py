from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ItemPerdido, ItemAchado, Perfil

# --------------------------
# PÁGINA INICIAL
# --------------------------
def index(request):
    return render(request, 'app/cadastro_user.html')

def cadastro_user(request):
    return render(request, 'app/cadastro_user.html')


# --------------------------
# LOGIN E PERFIL
# --------------------------
@login_required
def perfil(request):
    return render(request, 'app/perfil.html', {"usuario": request.user})

@login_required
def meus_cadastros(request):
    return render(request, 'app/meus_cadastros.html')


# --------------------------
# PÁGINAS DE LISTAGEM
# --------------------------
def perdidos(request):
    itens = ItemPerdido.objects.all()
    return render(request, 'app/perdidos.html', {'itens': itens})

def achados(request):
    itens = ItemAchado.objects.all().order_by('-id')
    return render(request, 'app/achados.html', {'itens': itens})


# --------------------------
# CADASTRAR ITENS
# --------------------------
def cadastrar_item(request):
    if request.method == 'POST':
        tipo = request.POST.get('formType')
        nome = request.POST.get('nome')
        desc = request.POST.get('descricao')
        categoria = request.POST.get('categoria')
        local = request.POST.get('local')
        data = request.POST.get('data')
        foto = request.FILES.get('foto')

        if tipo == "encontrado":
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

        return redirect('index')

    return render(request, 'app/cadastro.html')


def voltar(request):
    return redirect('index')


# --------------------------
# CADASTRO DE USUÁRIO
# --------------------------
def registrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma = request.POST.get('confirmaSenha')
        tipo = request.POST.get('userType')

        if senha != confirma:
            messages.error(request, "As senhas não coincidem.")
            return redirect('cadastrar_usuario')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Esse e-mail já está cadastrado.")
            return redirect('cadastrar_usuario')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome
        )

        Perfil.objects.create(user=user, tipo=tipo)

        messages.success(request, "Conta criada com sucesso!")
        return redirect('login')

    return render(request, 'app/cadastro_user.html')
def cadastro_user(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma = request.POST.get('confirmaSenha')
        tipo = request.POST.get('userType')

        # Validações
        if senha != confirma:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'app/cadastro_user.html')

        if User.objects.filter(username=email).exists():
            messages.error(request, "E-mail já cadastrado.")
            return render(request, 'app/cadastro_user.html')

        # Criar usuário
        user = User.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome
        )

        # Criar perfil associado
        perfil = Perfil.objects.create(
            user=user,
            tipo=tipo
        )

        messages.success(request, "Conta criada com sucesso! Faça login.")
        return redirect('login')

    return render(request, 'app/cadastro_user.html')