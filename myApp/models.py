from django.db import models
import sys,os
# Create your models here.
class Usuario(models.Model):
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


