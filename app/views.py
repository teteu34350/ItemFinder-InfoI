from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ItemPerdido, ItemAchado, Perfil
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Perfil 
from django.contrib.auth import update_session_auth_hash


# --------------------------
# PÁGINA INICIAL
# --------------------------
def index(request):
    return render(request, 'app/index.html')

def inicio(request):
    return render(request, 'app/cadastro.html')

# --------------------------
# LOGIN E PERFIL
# --------------------------
@login_required
def meu_perfil(request):
    # Usando .perfil para acessar o modelo Perfil associado ao User.
    # Esta linha pode falhar se o Perfil não foi criado no registro, 
    # mas se o 'perfil' já foi criado em outra view (como o 'perfil' abaixo), funciona.
    try:
        perfil = request.user.perfil
    except Perfil.DoesNotExist:
        # Cria um perfil básico se não existir (garante que não quebre)
        perfil = Perfil.objects.create(user=request.user, tipo='aluno')

    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        tipo = request.POST.get("tipo")
        bio = request.POST.get("bio")
        matricula = request.POST.get("matricula")

        # dividir nome
        partes_nome = nome.split()
        request.user.first_name = partes_nome[0] if partes_nome else ''
        request.user.last_name = " ".join(partes_nome[1:]) if len(partes_nome) > 1 else ''
        request.user.email = email
        request.user.save()

        perfil.telefone = telefone
        perfil.tipo = tipo
        perfil.bio = bio
        perfil.matricula = matricula
        perfil.save()

        messages.success(request, "Perfil atualizado com sucesso!")
        return redirect("meu_perfil")

    return render(request, "app/perfil.html", {"perfil": perfil})

@login_required
def perfil(request):
    # Uso do 'perfil' como nome de variável é mantido para consistência
    try:
        perfil_obj = Perfil.objects.get(user=request.user)
    except Perfil.DoesNotExist:
        perfil_obj = Perfil.objects.create(user=request.user, tipo='aluno') # Cria se não existir

    if request.method == "POST":
        # Atualizar informações do usuário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        tipo = request.POST.get('tipo')
        matricula = request.POST.get('matricula')
        bio = request.POST.get('bio')
        senha_atual = request.POST.get('senhaAtual')
        nova_senha = request.POST.get('novaSenha')
        confirma_senha = request.POST.get('confirmaSenha')

        # Atualizar dados básicos
        if nome:
            partes_nome = nome.split()
            request.user.first_name = partes_nome[0] if partes_nome else ''
            request.user.last_name = " ".join(partes_nome[1:]) if len(partes_nome) > 1 else ''
        
        request.user.email = email
        request.user.save()

        perfil_obj.telefone = telefone
        perfil_obj.tipo = tipo
        perfil_obj.matricula = matricula
        perfil_obj.bio = bio
        perfil_obj.save()

        # Alterar senha, se preenchida
        if nova_senha:
            if request.user.check_password(senha_atual):
                if nova_senha == confirma_senha:
                    request.user.set_password(nova_senha)
                    request.user.save()
                    update_session_auth_hash(request, request.user) # mantém logado
                    messages.success(request, "Senha alterada com sucesso!")
                else:
                    messages.error(request, "As senhas não conferem.")
            else:
                messages.error(request, "Senha atual incorreta.")
        
        # O alert de sucesso só deve aparecer se a senha não tiver dado erro
        if not nova_senha or (nova_senha and nova_senha == confirma_senha and request.user.check_password(senha_atual)):
            messages.success(request, "Perfil atualizado com sucesso!")
            
        return redirect('perfil')

    return render(request, 'app/perfil.html', {'perfil': perfil_obj})

# --------------------------
# LISTAGEM
# --------------------------
def perdidos(request):
    itens = ItemPerdido.objects.all()
    return render(request, 'app/perdidos.html', {'itens': itens})

def achados(request):
    itens = ItemAchado.objects.all().order_by('-id')
    return render(request, 'app/achados.html', {'itens': itens})


# --------------------------
# CADASTRAR ITENS
@login_required
def cadastrar_item(request):
    if request.method == 'POST':
        tipo = request.POST.get('formType')
        nome = request.POST.get('nome')
        desc = request.POST.get('descricao')
        categoria = request.POST.get('categoria')
        local = request.POST.get('local')
        data = request.POST.get('data')
        foto = request.FILES.get('foto')

        # ITEM ACHADO
        if tipo == "encontrado":
            ItemAchado.objects.create(
                nome=nome,
                desc=desc,
                categoria=categoria,
                local=local,
                data=data,
                foto=foto,
                user=request.user
            )

        # ITEM PERDIDO
        else:
            ItemPerdido.objects.create(
                nome=nome,
                desc=desc,
                categoria=categoria,
                local=local,
                data=data,
                foto=foto,
                recompensa=request.POST.get('recompensa'),
                tipoContato=request.POST.get('tipoContato'),
                contato=request.POST.get('contato'),
                user=request.user
            )

        return redirect('home')

    return render(request, 'app/cadastro.html')

def voltar(request):
    return redirect('index')


# --------------------------
# LOGIN
# --------------------------

def login_user(request):
    if request.method == "POST":
        # Usamos o email como username
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        user = authenticate(request, username=email, password=senha)

        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('index')
        else:
            # Verifica se o e-mail existe
            from django.contrib.auth.models import User
            if not User.objects.filter(username=email).exists():
                messages.error(request, "E-mail não encontrado.")
            else:
                messages.error(request, "Senha incorreta.")

    return render(request, "app/login.html")


# --------------------------
# CADASTRO DE USUÁRIO (1ª versão)
# --------------------------
def registrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get("telefone")
        senha = request.POST.get('senha')
        confirma = request.POST.get('confirmaSenha')
        tipo = request.POST.get('userType')

        if senha != confirma:
            messages.error(request, "As senhas não coincidem.")
            return redirect('cadastrar_usuario')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Esse e-mail já está cadastrado.")
            return redirect('cadastrar_usuario')

        # 1. Cria o objeto User (sem o telefone)
        user = User.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome,
            # Linha removida: telefone=telefone, <-- O User padrão do Django não tem esse campo
        )

        # 2. Cria o objeto Perfil e ADICIONA O TELEFONE AQUI
        Perfil.objects.create(
            user=user, 
            tipo=tipo, 
            telefone=telefone # <-- CORREÇÃO: Passa o telefone para o Perfil
        )

        messages.success(request, "Conta criada com sucesso!")
        return redirect('login')

    return render(request, 'app/cadastro_user.html')


# --------------------------
# CADASTRO DE USUÁRIO (2ª versão) — NÃO APAGUEI
# RENOMEADA PARA NÃO DAR ERRO
# --------------------------
def cadastro_user(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone') # <-- CORREÇÃO: Pegar o telefone do POST
        senha = request.POST.get('senha')
        confirma = request.POST.get('confirmaSenha')
        tipo = request.POST.get('userType')

        if senha != confirma:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'app/cadastro_user.html')

        if User.objects.filter(username=email).exists():
            messages.error(request, "E-mail já cadastrado.")
            return render(request, 'app/cadastro_user.html')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome
        )

        Perfil.objects.create(
            user=user,
            tipo=tipo,
            telefone=telefone # <-- CORREÇÃO: Passa o telefone para o Perfil
        )

        messages.success(request, "Conta criada com sucesso! Faça login.")
        return redirect('login')

    return render(request, 'app/cadastro_user.html')
from django.contrib.auth import logout

@login_required
def deletar_conta(request):
    if request.method == "POST":
        user = request.user
        logout(request)# desloga o usuário antes de excluir
        user.delete()
        messages.success(request, "Conta deletada com sucesso!")
        return redirect('home')
    return redirect('perfil')

@login_required
def meus_cadastros(request):
    perdidos = ItemPerdido.objects.filter(user=request.user).order_by('-criado_em')
    achados = ItemAchado.objects.filter(user=request.user).order_by('-criado_em')

    cadastros = list(perdidos) + list(achados)
    cadastros.sort(key=lambda x: x.criado_em, reverse=True)

    return render(request, 'app/meus_cadastros.html', {'cadastros': cadastros})
