from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin


#só existe esse trecho para que na página do admin a APAREÇA o campo novo que criamos para o usuário (filmes_vistos)

campos = list(UserAdmin.fieldsets)   #transformando campos do UserAdmin em lista
campos.append(
    ("Histórico", {'fields': ('filmes_vistos',)})   #adicionando campos desejados
)

UserAdmin.fieldsets = tuple(campos)  #volta a ser uma tupla com o novo dado

admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)


