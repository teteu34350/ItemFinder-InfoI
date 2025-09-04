from django.db import models

# Create your models here.
class ItemPerdido(models.Model):
    nome = models.CharField(max_length=100,verbose_name = "Nome do Item Perdido")
    desc = models.TextField(max_length=250, verbose_name="Descrição", default="Sem descrição")
    foto = models.ImageField(upload_to="fotos/",null=True,blank=True)
    data = models.DateField(verbose_name="Data que o item foi Perdido",null=True,blank=True)
    OPCOES = [
        ("Biblioteca","Biblioteca"),
        ("Predio do Café","Predio do Café"),
        ("Agronomia","Agronomia"),
        ("Celin","Celin"),
        ("Predio da informatica","Predio da informatica"),
        ("Refeitorio","Refeitorio"),
        ("Predio H","Predio H"),
        ("Lanchonete","Lanchonete"),
        ("Coopam","Coopam"),
        ("Quadra","Quadra"),
        ("Poli esoportivo","Poli esportivo"),
        ("Tatame","Tatame"),
        ("Academia","Academia"),
        ("Selca","Selca"),
        ("Sala de jogos","Sala de jogos"),
        ("Alojamento A","Alojamento A"),
        ("Alojamento B","Alojamento B"),
        ("Alojamento C","Alojamento C"),
        ("Hospital Veterinario","Hospital Veterinario"),
        ("Z3 de Leite","Z3 de leite"),
        ("Z3 de corte","Z3 de corte"),
        ("Caprino","Caprino"),
        ("Suino","Suino"),
        ("Cunicultura","Cunicultura"),
        ("Cecaes","Cecaes"),
    ]
    local = models.CharField(choices = OPCOES,default = "Não sei aonde perdi")
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

    categoria = models.CharField(choices = OPCOES_CAT,default = "Sem categoria")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "PerdiMeuItem"

class ItemAchado(models.Model):
    nome = models.CharField(max_length=100,verbose_name = "Nome do Item Achado")
    desc = models.TextField(max_length=250, verbose_name="Descrição", default="Sem descrição")
    foto = models.ImageField(upload_to="fotos/",null=True,blank=True)
    data = models.DateField(verbose_name="Data que o item foi Perdido",null=True,blank=True)
    OPCOES = [
        ("Biblioteca","Biblioteca"),
        ("Predio do Café","Predio do Café"),
        ("Agronomia","Agronomia"),
        ("Celin","Celin"),
        ("Predio da informatica","Predio da informatica"),
        ("Refeitorio","Refeitorio"),
        ("Predio H","Predio H"),
        ("Lanchonete","Lanchonete"),
        ("Coopam","Coopam"),
        ("Quadra","Quadra"),
        ("Poli esoportivo","Poli esportivo"),
        ("Tatame","Tatame"),
        ("Academia","Academia"),
        ("Selca","Selca"),
        ("Sala de jogos","Sala de jogos"),
        ("Alojamento A","Alojamento A"),
        ("Alojamento B","Alojamento B"),
        ("Alojamento C","Alojamento C"),
        ("Hospital Veterinario","Hospital Veterinario"),
        ("Z3 de Leite","Z3 de leite"),
        ("Z3 de corte","Z3 de corte"),
        ("Caprino","Caprino"),
        ("Suino","Suino"),
        ("Cunicultura","Cunicultura"),
        ("Cecaes","Cecaes"),
    ]
    local = models.CharField(choices = OPCOES,default = "Sem local")
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

    categoria = models.CharField(choices = OPCOES_CAT,default = "Sem categoria")

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "AcheiUmItem"


