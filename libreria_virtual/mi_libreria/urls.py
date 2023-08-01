from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("libros/", views.listar_libros, name='lista_libros'),
    path("generos/", views.listar_generos, name='lista_generos'),
    path("autores/", views.listar_autores, name='lista_autores'),
]