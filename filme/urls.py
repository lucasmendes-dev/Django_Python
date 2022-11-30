from django.urls import path, include
from .views import  HomeFilmes, HomePage, DetalhesFilme, PesquisaFilme, PaginaPerfil
from django.contrib.auth import views as auth_view


app_name = 'filme'    #namespace no arquivo urls do projeto(dir hashflix)

urlpatterns = [    
    path('', HomePage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name='detalhesfilme'),
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html') , name="login"),    #classe pré definida pelo próprio Django
    path('logout/', auth_view.LogoutView.as_view(template_name='login.html') , name="logout"),    
    path('editarperfil/', PaginaPerfil.as_view(), name='editarperfil'),
]   