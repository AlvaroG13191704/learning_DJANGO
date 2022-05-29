
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView
from django.shortcuts import get_object_or_404, redirect, render

#Import models
from persona.models import Empleado
#Import forms
from persona.forms import EmpleadoForm

# Create your views here.
##THE HOME PAGE
def home(request):
    #Take all 
    return render(request,'inicio.html')

#EMPLEADO
#Vista basada en clases
class listaEmpleados(ListView):
    template_name = 'lista_empleados.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        key_word = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            first_name__icontains = key_word
        )
        return lista

#Lista empleados by area
class ListaEmpleadosByArea(ListView):
    template_name = 'personas/lista_area.html'
    context_object_name = 'empleados'
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__short_name = area
        )
        return lista
#Lista empleados admin
class listaEmpleadosAdmin(ListView):
    model = Empleado
    template_name = 'lista_empleados_admin.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'

##CRUD
#Crear

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "personas/empleado_add.html"
    fields = '__all__'
    success_url = reverse_lazy('lista_empleados')

#Actualizar
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "personas/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
    ]
    success_url = reverse_lazy('empleados_admin')

##funciones
#Eliminar
def EmpleadoDeleteView(request,pk):
    empleado = get_object_or_404(Empleado,pk=pk)
    if empleado:
        empleado.delete()
    return redirect('empleados_admin')


#Ver empleado
def verEmpleado(request, id):
    #Traemos al empleado
    empleado = get_object_or_404(Empleado,pk=id)
    return render(request,'detail_empleado.html',{'empleado':empleado})
