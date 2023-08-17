from django.urls import path

from . import views

urlpatterns = [
    path("articulos/", views.listar_articulos, name='lista_articulos'),
]

