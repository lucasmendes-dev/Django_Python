from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser   #import de usuário


LISTA_CATEGORIAS = (
    ("analises", "Análises"),
    ("programacao", "Programação"),
    ("apresentacao", "Apresentação"),
    ("outros", "Outros")
)

#Lembrar de cadastrar suas models no arquivo admin.py para poder usá-las no /admin 

class Filme(models.Model):    
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    vizualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo
    

class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE) 
    titulo = models.CharField(max_length=100)
    video = models.URLField(default='your link...')
    
    def __str__(self):
        return self.filme.titulo + " - " + self.titulo
    
    
class Usuario(AbstractUser):
    #criar apenas campos novos
    filmes_vistos = models.ManyToManyField("Filme")   #nome da clase para se relacionar