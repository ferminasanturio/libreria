from django.urls import path

from . import views

urlpatterns = [
    path("about/", views.about, name='about_me'),
    path("pages/", views.listar_articulos, name='lista_articulos'),
    path('pages/<int:pk>/', views.ArticuloDetailView.as_view(), name='ver_articulos'),
    path("crear_articulo/", views.crear_articulos, name='crear_articulos'),
    path('eliminar-articulo/<int:id>/', views.eliminar_articulos, name="eliminar_articulos"),
    path('editar-articulo/<int:id>/', views.editar_articulos, name="editar_articulos"),
]

