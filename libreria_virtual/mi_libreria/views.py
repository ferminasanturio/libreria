from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Libro, Generos, Autores
from .forms import AutorFormulario, LibroFormulario, GeneroFormulario


def inicio(request):
    http_response = render(
        request=request,
        template_name= 'mi_libreria/inicio.html',
        context={},
    )
    return http_response

@login_required
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

@login_required
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

@login_required
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

def crear_libros(request):
   if request.method == "POST":
       formulario = LibroFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  
           nombre = data["nombre"]
           genero = data["genero"]
           sub_genero = data["sub_genero"]
           autor = data["autor"]
           resumen = data["resumen"]
           anio = data["anio"]
           curso = Libro(nombre=nombre, genero=genero, sub_genero=sub_genero, autor=autor, resumen=resumen, anio=anio)
           curso.save()

           url_exitosa = reverse('lista_libros')
           return redirect(url_exitosa)
   else: 
       formulario = LibroFormulario()
   http_response = render(
       request=request,
       template_name='mi_libreria/crear_libros.html',
       context={'formulario': formulario}
   )
   return http_response

def crear_generos(request):
   if request.method == "POST":
       formulario = GeneroFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  
           nombre = data["nombre"]
           sub_genero = data["sub_genero"]
           curso = Generos(nombre=nombre,sub_genero=sub_genero)
           curso.save()

           url_exitosa = reverse('lista_generos')
           return redirect(url_exitosa)
   else: 
       formulario = GeneroFormulario()
   http_response = render(
       request=request,
       template_name='mi_libreria/crear_generos.html',
       context={'formulario': formulario}
   )
   return http_response

def crear_autores(request):
   if request.method == "POST":
       formulario = AutorFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  
           nombre = data["nombre"]
           apellido = data["apellido"]
           fecha_nacimiento = data["fecha_nacimiento"]      
           bio = data["bio"]     
           curso = Autores(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, bio=bio)
           curso.save()

           url_exitosa = reverse('lista_autores')
           return redirect(url_exitosa)
   else: 
       formulario = AutorFormulario()
   http_response = render(
       request=request,
       template_name='mi_libreria/crear_autores.html',
       context={'formulario': formulario}
   )
   return http_response

def buscar_libros(request):
    if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       libros = Libro.objects.filter(nombre__contains=busqueda)
       contexto = {
           "libros": libros,
       }
       http_response = render(
           request=request,
           template_name='mi_libreria/lista_libros.html',
           context=contexto,
       )
       return http_response

def eliminar_libro(request, id):
   libro = Libro.objects.get(id=id)
   if request.method == "POST":
       libro.delete()
       url_exitosa = reverse('lista_libros')
       return redirect(url_exitosa)
   
def eliminar_autor(request, id):
   autor = Autores.objects.get(id=id)
   if request.method == "POST":
       autor.delete()
       url_exitosa = reverse('lista_autores')
       return redirect(url_exitosa)
   
def eliminar_genero(request, id):
   genero = Generos.objects.get(id=id)
   if request.method == "POST":
       genero.delete()
       url_exitosa = reverse('lista_generos')
       return redirect(url_exitosa)
   
def editar_libro(request, id):
   libro = Libro.objects.get(id=id)
   if request.method == "POST":
       formulario = LibroFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           libro.nombre = data['nombre']
           libro.autor = data['autor']
           libro.save()
           url_exitosa = reverse('lista_libros')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': libro.nombre,
           'autor': libro.autor,
       }
       formulario = LibroFormulario(initial=inicial)
   return render(
       request=request,
       template_name='mi_libreria/crear_libros.html',
       context={'formulario': formulario},
   )

def editar_autor(request, id):
   autor = Autores.objects.get(id=id)
   if request.method == "POST":
       formulario = AutorFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           autor.nombre = data['nombre']
           autor.apellido = data['apellido']
           autor.save()
           url_exitosa = reverse('lista_autores')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': autor.nombre,
           'apellido': autor.apellido,
       }
       formulario = AutorFormulario(initial=inicial)
   return render(
       request=request,
       template_name='mi_libreria/crear_autores.html',
       context={'formulario': formulario},
   )

def editar_genero(request, id):
   genero = Generos.objects.get(id=id)
   if request.method == "POST":
       formulario = GeneroFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           genero.nombre = data['nombre']
           genero.sub_genero = data['sub_genero']
           genero.save()
           url_exitosa = reverse('lista_generos')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': genero.nombre,
           'sub_genero': genero.sub_genero,
       }
       formulario = GeneroFormulario(initial=inicial)
   return render(
       request=request,
       template_name='mi_libreria/crear_generos.html',
       context={'formulario': formulario},
   )



