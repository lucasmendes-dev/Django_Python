from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


#CBV - Class Based Views

class HomePage(TemplateView):
   template_name = "homepage.html"


class HomeFilmes(ListView):
   template_name = "homefilmes.html"
   model = Filme   #passa uma lista com o nome: 'object_list' para o template
   # object_list -> lista de itens do modelo
   

class DetalhesFilme(DetailView):
   template_name = "detalhesfilme.html"
   model = Filme
   # object -> 1 item do modelo
 
   def get_context_data(self, **kwargs):
      context = super(DetalhesFilme, self).get_context_data(**kwargs)
      #filtrar usando a coluna 'categoria' da tabela filmes
      filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)
      context['filmes_relacionados'] = filmes_relacionados
      return context




#FBV - Function Based Views
#***exemplo usando functions (FBV)***

#def homefilmes(request):
#   context = {}
#   lista_filmes = Filme.objects.all()
#   context['lista_filmes'] = lista_filmes
#   
#   return render(request, 'homefilmes.html', context)
