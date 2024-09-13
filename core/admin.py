from django.contrib import admin
from .models import Poeme

class PoemeAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur')  # affiche le titre et l'auteur dans la liste des poèmes
    search_fields = ('titre', 'auteur')  # ajoute un champ de recherche sur le titre et l'auteur
    list_filter = ('auteur',)  # permet de filtrer les poèmes par auteur

admin.site.register(Poeme, PoemeAdmin)
