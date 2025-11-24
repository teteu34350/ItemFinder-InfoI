from django.db import models
from django.contrib.auth.models import User


# ------------------------------
# TABELA: Item Perdido
# ------------------------------
class ItemPerdido(models.Model):
    nome = models.CharField(max_length=100)
    desc = models.TextField()
    local = models.CharField(max_length=100)
    data = models.DateField()
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    tipoContato = models.CharField(max_length=20)
    contato = models.CharField(max_length=100)
    recompensa = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    @property
    def tipo_item(self):
        return "perdido"


# ------------------------------
# TABELA: Item Achado
# ------------------------------
class ItemAchado(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Item Achado")
    desc = models.TextField(max_length=250, verbose_name="Descrição", default="Sem descrição")
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    data = models.DateField(verbose_name="Data que o item foi Perdido", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    OPCOES = [
        ("Biblioteca", "Biblioteca"),
        ("Predio do Café", "Predio do Café"),
        ("Agronomia", "Agronomia"),
        ("Celin", "Celin"),
        ("Predio da informatica", "Predio da informatica"),
        ("Refeitorio", "Refeitorio"),
        ("Predio H", "Predio H"),
        ("Lanchonete", "Lanchonete"),
        ("Coopam", "Coopam"),
        ("Quadra", "Quadra"),
        ("Poli esportivo", "Poli esportivo"),
        ("Tatame", "Tatame"),
        ("Academia", "Academia"),
        ("Selca", "Selca"),
        ("Sala de jogos", "Sala de jogos"),
        ("Alojamento A", "Alojamento A"),
        ("Alojamento B", "Alojamento B"),
        ("Alojamento C", "Alojamento C"),
        ("Hospital Veterinario", "Hospital Veterinario"),
        ("Z3 de Leite", "Z3 de leite"),
        ("Z3 de corte", "Z3 de corte"),
        ("Caprino", "Caprino"),
        ("Suino", "Suino"),
        ("Cunicultura", "Cunicultura"),
        ("Cecaes", "Cecaes"),
    ]
    local = models.CharField(max_length=50, choices=OPCOES, default="Biblioteca")

    OPCOES_CAT = [
        ("Roupa", "Roupa"),
        ("Eletrônico", "Eletrônico"),
        ("Livro", "Livro"),
        ("Documento", "Documento"),
        ("Chave", "Chave"),
        ("Acessório", "Acessório"),
        ("Brinquedo", "Brinquedo"),
        ("Mochila", "Mochila"),
        ("Celular", "Celular"),
        ("Óculos", "Óculos"),
    ]
    categoria = models.CharField(max_length=50, choices=OPCOES_CAT, default="Roupa")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "AcheiUmItem"

    @property
    def tipo_item(self):
        return "encontrado"


# ------------------------------
# TABELA: Perfil
# ------------------------------
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20)

    telefone = models.CharField(max_length=15, blank=True, null=True)
    matricula = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name
