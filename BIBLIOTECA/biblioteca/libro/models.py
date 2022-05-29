from django.db import models
from autor.models import Autor
from .managers import LibroManager,CategoriaManager
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30 )
    objects = CategoriaManager()
    def __str__(self):
        return str(self.id)+"-"+self.nombre

class Libro(models.Model):
    #Con related_name me crea un parametro para llegar de categoria a libro
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField( max_length=50)
    fecha = models.DateField('fecha_de_lazamiento', auto_now=False, auto_now_add=False)
    portada = models.ImageField(upload_to="portada")
    visitas = models.PositiveIntegerField( default=0)
    stok = models.PositiveBigIntegerField(default=0)
    #Manger
    objects = LibroManager()

    #Class meta
    """
    Es todo aquello que dentro de nuestro modelo no es un atributo o tabla de la db
    """
    

    def __str__(self):
        return f'{self.id}  {self.titulo}'

