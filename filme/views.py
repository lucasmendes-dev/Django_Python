from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin   #lib para controlar o acesso de pág. somente quando o usuário estiver logado


#CBV - Class Based Views

class HomePage(TemplateView):   
   template_name = "homepage.html"
   
   def get(self, request, *args, **kwargs):
      if request.user.is_authenticated:
         return redirect('filme:homefilmes')   #nomeapp.urlname
      else:
         return super().get(request, *args, **kwargs)   #redireciona para a homepage


class HomeFilmes(LoginRequiredMixin, ListView):
   template_name = "homefilmes.html"
   model = Filme   #passa uma lista com o nome: 'object_list' para o template
   # object_list -> lista de itens do modelo
   

class DetalhesFilme(LoginRequiredMixin, DetailView):
   template_name = "detalhesfilme.html"
   model = Filme
   # object -> 1 item do modelo
   
   
   def get(self, request, *args, **kwargs):
      filme = self.get_object()
      filme.vizualizacoes += 1
      filme.save()      
      usuario = request.user
      usuario.filmes_vistos.add(filme)
      return super(DetalhesFilme, self).get(request, *args, **kwargs) #redireciona para a url final
      
 
   def get_context_data(self, **kwargs):
      context = super(DetalhesFilme, self).get_context_data(**kwargs)
      #filtrar usando a coluna 'categoria' da tabela filmes
      filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)
      context['filmes_relacionados'] = filmes_relacionados
      return context


class PesquisaFilme(LoginRequiredMixin, ListView):
   template_name = "pesquisa.html"
   model = Filme
   
   
   def get_queryset(self):
      pesquisa = self.request.GET.get('query')  #nome do 'id' ou 'name' definido no html
      if pesquisa:
         object_list = Filme.objects.filter(titulo__icontains=pesquisa) #nomecoluna__icontains
         return object_list
      else:
         return None
      
      
class PaginaPerfil(LoginRequiredMixin, TemplateView):
   template_name = "editarperfil.html"   
   
   
class CriarConta(FormView):
   template_name = "criarconta.html"
   form_class = CriarContaForm
   
   def form_valid(self, form):
      form.save()
      return super().form_valid(form)
   
   def get_success_url(self):
      return reverse('filme:login')



#FBV - Function Based Views
#***exemplo usando functions (FBV)***

#def homefilmes(request):
#   context = {}
#   lista_filmes = Filme.objects.all()
#   context['lista_filmes'] = lista_filmes
#   
#   return render(request, 'homefilmes.html', context)
