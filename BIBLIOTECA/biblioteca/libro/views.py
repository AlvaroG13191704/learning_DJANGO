from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Libro
# Create your views here.
def listaLibros(request):
    kword = request.GET.get('kword','')
    fecha1 = request.GET.get('fecha1','')
    fecha2 = request.GET.get('fecha2','')
    print(kword)
    print(fecha1)
    print(fecha2)
    if fecha1 and fecha2:
        libros = Libro.objects.listar_libro(kword,fecha1,fecha2)
        return render(request,'libro/lista.html',{'libros':libros})
    else:
        libros = Libro.objects.filtrar_lista(kword)
        return render(request,'libro/lista.html',{'libros':libros})

def listaLibros2(request):
    libros = Libro.objects.listar_categoria("3")
    return render(request,'libro/categoria.html',{'libros':libros})

#detail
def ver_libro(request,id):
    libro = get_object_or_404(Libro, pk=id)
    return render(request,'libro/libro.html',{'libro':libro})