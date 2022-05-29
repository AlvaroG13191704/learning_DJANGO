from django.db import models
from .managers import AutorManager

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField( max_length=50)
    apellidos = models.CharField( max_length=50)
    nacionalidad = models.CharField( max_length=20)
    edad = models.PositiveIntegerField( default=0)
    #Abstrac es para crear la clase que sera el padre de las demas
    class Meta:
        abstract = True  
    def __str__(self):
        return f'{self.id}  {self.nombres} {self.apellidos}'
        
class Autor(Persona):
    objects = AutorManager()
    
