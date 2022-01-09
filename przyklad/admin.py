# prezentacja/przyklad/admin.py

from django.contrib import admin
from .models import Autor, Ksiazka

@admin.register(Autor)
class AutorAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'imie_nazwisko')

@admin.register(Ksiazka)
class KsiazkaAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'tytul', 'autor')