from asyncio.windows_events import NULL
from distutils.command.upload import upload
from tabnanny import verbose
from turtle import update
from django.db import models

# Create your models here.

class CategoriaProd(models.Model):

    nombre=models.CharField(max_length=50)

    created=models.DateTimeField(auto_now_add=True)

    updated=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name:'CategoriaProd'
        verbose_name_plural:'CategoriaProd'

    def __str__(self):

        return self.nombre


class Producto(models.Model):

    nombre=models.CharField(max_length=50)

    categoria=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)

    imagen=models.ImageField(upload_to="tienda")

    precio=models.FloatField()

    disponibilidad=models.BooleanField(default=True)

    created=models.DateTimeField(auto_now_add=True)

    updated=models.DateTimeField(auto_now_add=True)


    class Meta:

        verbose_name:'Producto'
        verbose_name_plural:'Producto'

    

