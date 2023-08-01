from django.contrib import admin

from .models import Libro, Generos, Autores

admin.site.register(Libro)
admin.site.register(Generos)
admin.site.register(Autores)
