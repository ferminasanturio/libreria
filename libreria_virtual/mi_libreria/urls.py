from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("libros/", views.listar_libros, name='lista_libros'),
    path("generos/", views.listar_generos, name='lista_generos'),
    path("autores/", views.listar_autores, name='lista_autores'),
    path("crear_libro/", views.crear_libros, name='crear_libros'),
    path("crear_genero/", views.crear_generos, name='crear_generos'),
    path("crear_autor/", views.crear_autores, name='crear_autores'),
    path("buscar_libro/", views.buscar_libros, name='buscar_libros'),
]