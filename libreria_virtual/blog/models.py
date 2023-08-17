from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=64)
    subtitulo = models.CharField(max_length=64)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=64)
    fecha = models.DateField()
    


