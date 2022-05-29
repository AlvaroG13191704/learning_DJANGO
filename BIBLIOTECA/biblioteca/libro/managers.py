
from django.db import models
from django.db.models import Q,Count

class LibroManager(models.Manager):
    #Filtar libro
    def filtrar_lista(self,kword):
        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('2000-01-01','2020-01-01')
        )
        return resultado    
    #Recibir fecha, validar y filtrar
    def listar_libro(self,kword,fecha1,fecha2):
        
        resultado = self.filter(
            titulo__icontains = kword,
            fecha__range = (fecha1,fecha2)
        )
        return resultado

    #filtar por categoria por su foreingkey
    def listar_categoria(self,categoria):
        return self.filter(categoria__id=categoria).order_by('titulo')

    #registrar o agregar un autor en un determinado registro
    def add_autor_libro(self,libro_id,autor):
        libro = self.get(id=libro_id)
        #Para elimina es lo mismo, se usa remove
        libro.autores.add(autor)
        return libro
    #aggregate para calcular las veces que fue prestado un libro
    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_prestamos=Count('libro_prestado')
        )
        return resultado

class CategoriaManager(models.Manager):
    #con el related_name entramos al models de Libro y podemos navegar hacia cualquier lado, en este caso autores
    def categoria_autor(self,autor):
        return self.filter(
            categoria_libro__autores__id=autor
        )
    """
    Annotate es como un filter el cual puede contar la cantidad de libros que tiene
    esa categoria, creando un nuevo parametro ademas del que ya existe en models o en pocas palabras...
    "contar el numero de cosas que existen en un diferente grupo de opciones"
    el ralated_name sirve para ir de retroceso entre bases relacionadas
    """
    def listar_categoria_libros(self):
        resultado = self.annotate(
            num_libros=Count("categoria_libro")
        )
        for r in resultado:
            print("++++")
            print(r,r.num_libros)
        return resultado

    