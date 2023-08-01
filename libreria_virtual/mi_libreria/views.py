from django.shortcuts import render

from django.http import HttpResponse

from mi_libreria.models import Libro, Generos, Autores

def inicio(request):
    return HttpResponse("Hello, world. You're at the library index.")

def listar_libros(request):
    contexto = {
        "libros": Libro.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='mi_biblioteca/lista_libros.html',
        context=contexto,
    )
    return http_response

def listar_generos(request):
    contexto = {
        "generos": Generos.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='mi_biblioteca/lista_generos.html',
        context=contexto,
    )
    return http_response

def listar_autores(request):
    contexto = {
        "autores": Autores.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='mi_biblioteca/lista_autores.html',
        context=contexto,
    )
    return http_response

