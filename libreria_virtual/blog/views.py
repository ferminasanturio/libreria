from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Articulo
from .forms import ArticuloFormulario

def listar_articulos(request):
        contexto = {
            "articulos": Articulo.objects.all(),
        }
        http_response = render(
            request=request,
            template_name='blog/lista_articulos.html',
            context=contexto,
        )
        return http_response

def crear_articulos(request):
   if request.method == "POST":
       formulario = ArticuloFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  
           titulo = data["titulo"]
           subtitulo = data["subtitulo"]
           cuerpo = data["cuerpo"]
           autor = data["autor"]
           fecha = data["fecha"]
           articulo = Articulo(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha)
           articulo.save()

           url_exitosa = reverse('lista_articulos')
           return redirect(url_exitosa)
   else: 
       formulario = ArticuloFormulario()
   http_response = render(
       request=request,
       template_name='blog/crear_articulos.html',
       context={'formulario': formulario}
   )
   return http_response
