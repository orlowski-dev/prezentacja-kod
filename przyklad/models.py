# prezentacja/przyklad/models.py

from django.db import models

class Autor(models.Model):
    imie_nazwisko = models.CharField(
        max_length=254,
        verbose_name='Imię i Nazwisko Autora',
    )

    def __str__(self) -> str:
        return self.imie_nazwisko

class Ksiazka(models.Model):
    autor = models.ForeignKey(
        to=Autor,
        verbose_name='Author',
        on_delete=models.CASCADE,
    )
    tytul = models.CharField(
        max_length=254,
        verbose_name='Tytuł'
    )

    def __str__(self) -> str:
        return f'{self.autor.imie_nazwisko} {self.tytul}'