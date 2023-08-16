from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name='inicio'),
    path("libros/", views.listar_libros, name='lista_libros'),
    path("generos/", views.listar_generos, name='lista_generos'),
    path("autores/", views.listar_autores, name='lista_autores'),
    path("crear_libro/", views.crear_libros, name='crear_libros'),
    path("crear_genero/", views.crear_generos, name='crear_generos'),
    path("crear_autor/", views.crear_autores, name='crear_autores'),
    path("buscar_libro/", views.buscar_libros, name='buscar_libros'),
    path('eliminar-libro/<int:id>/', views.eliminar_libro, name="eliminar_libro"),
    path('eliminar-autor/<int:id>/', views.eliminar_autor, name="eliminar_autor"),
    path('eliminar-genero/<int:id>/', views.eliminar_genero, name="eliminar_genero"),
    path('editar-libro/<int:id>/', views.editar_libro, name="editar_libro"),
    path('editar-autor/<int:id>/', views.editar_autor, name="editar_autor"),
    path('editar-genero/<int:id>/', views.editar_genero, name="editar_genero"),
]