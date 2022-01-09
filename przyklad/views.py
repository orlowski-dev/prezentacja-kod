# prezentacja/przyklad/views.py
from django.shortcuts import render
from .models import Autor, Ksiazka

def przyklad(request):

    autorzy = Autor.objects.all()
    ksiazki = Ksiazka.objects.all()

    kontekst = {'autorzy': autorzy, 'ksiazki': ksiazki}

    return render(request, 'przyklad.html', kontekst)


