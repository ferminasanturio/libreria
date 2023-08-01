from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Libro, Generos, Autores

def inicio(request):
    http_response = render(
        request=request,
        template_name= 'mi_libreria/inicio.html',
        context={},
    )
    return http_response

def listar_libros(request):
    contexto = {
        "libros": Libro.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='mi_libreria/lista_libros.html',
        context=contexto,
    )
    return http_response

def listar_generos(request):
    contexto = {
        "generos": Generos.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='mi_libreria/lista_generos.html',
        context=contexto,
    )
    return http_response

def listar_autores(request):
    contexto = {
        "autores": Autores.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='mi_libreria/lista_autores.html',
        context=contexto,
    )
    return http_response

