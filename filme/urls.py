from django.urls import path, include
from .views import  HomeFilmes, HomePage, DetalhesFilme, PesquisaFilme


app_name = 'filme'    #namespace no arquivo urls do projeto(dir hashflix)

urlpatterns = [    
    path('', HomePage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name='detalhesfilme'),
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisafilme')
]