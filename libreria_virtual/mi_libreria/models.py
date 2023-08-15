from django.db import models
from django.contrib.auth.models import User
class Libro(models.Model):
    nombre = models.CharField(max_length=64)
    genero = models.CharField(max_length=64)
    sub_genero = models.CharField(max_length=64)
    autor = models.CharField(max_length=256)
    resumen = models.TextField()
    anio = models.IntegerField()
    creador = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE, related_name='libros_creados')


    def __str__(self):
        return f'{self.nombre}, {self.autor}'

class Generos(models.Model):
    nombre = models.CharField(max_length=32)
    sub_genero = models.CharField(max_length=128)
    creador = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE, related_name='generos_creados')

    def __str__(self):
        return f'{self.nombre}, {self.sub_genero}'

class Autores(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    creador = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE, related_name='autores_creados')

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
