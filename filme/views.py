from django.shortcuts import render
from .models import Filme

#FBV - Function Based Views
def homepage(request):
   return render(request, "homepage.html")

#CBV - Class Based Views
#class HomePage():
#  pass


def homefilmes(request):
   context = {}
   lista_filmes = Filme.objects.all()
   context['lista_filmes'] = lista_filmes
   
   return render(request, 'homefilmes.html', context)

