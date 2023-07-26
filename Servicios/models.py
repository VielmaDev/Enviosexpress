from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class Servicios(models.Model):

    titulo= models.CharField(max_length=50)

    contenido= models.CharField(max_length=50)

    image= models.ImageField(upload_to='Servicios')

    created= models.DateTimeField(auto_now_add=True)

    updated= models.DateTimeField(auto_now_add=True)

    class Meta():

        verbose_name= 'Servicios'

        verbose_name_plural='Servicios'

    def __str__(self):

        return self.titulo

