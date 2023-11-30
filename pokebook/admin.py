from django.contrib import admin

from .models import Pokename,Pokepost

class PokemonAdmin(admin.ModelAdmin):
    list_display=('id','name')
    list_display_links=('id','name')

class PokePostAdmin(admin.ModelAdmin):
    list_display=('id','name')
    list_display_links=('id', 'name')

admin.site.register(Pokename,)