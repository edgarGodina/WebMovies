from django.db import models
import sys,os
# Create your models here.
class Director(models.Model):
    """
        Clase Usuario que llevara consigo guardado = { id,email,nombre,apellidos,fecha de nacimiento , fecha de registro, password}

    """
    id = models.BigAutoField(primary_key = True)
    email = models.EmailField(max_length=100)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaDeNacimiento = models.DateTimeField()
    fechaDeRegistro = models.DateTimeField()
    password = models.CharField(max_length=30)


class Peliculas(models.Model):
    """
        Clase de peliculas que llevara consigo guardado {idpelicula,Nombrepelicula,año de filmacion,director(usuario),casaproductora,valorfilmacion}
    """
    idPelicula = models.BigAutoField(primary_key = True)
    idDirector = models.ForeignKey(Director,on_delete=models.CASCADE)
    nombreDePelicula = models.CharField(max_length=50)
    año = models.DateTimeField()
    casaProductora = models.CharField(max_length=60)
