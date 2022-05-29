from datetime import date

from django.shortcuts import render,redirect
from .models import Prestamo
from .forms import PrestamoForm, PrestamoMultipleForm
# Create your views here.

def registar_prestamo(request):
    #
    if request.method == 'POST':
        #Create a form instance
        form = PrestamoForm(request.POST)
        if form.is_valid():
            Prestamo.objects.create(
                lector = form.cleaned_data['lector'],
                libro = form.cleaned_data['libro'], 
                fecha_prestamo = date.today(),
                devuelto = False
            )
            return redirect('registrar_prestamo')
    else:
        form = PrestamoForm()
    #return
    return render(request,'lector/prestamoForm.html',{'form':form})

#forma de registro
"""
Este esta hecho por si ya fue creado nomas nos trae el prestamo,sino lo crea
"""
def addPrestamo(request):
    #
    if request.method == 'POST':
        #Create a form instance
        form = PrestamoForm(request.POST)
        if form.is_valid():
            obj,created = Prestamo.objects.get_or_create(
                lector = form.cleaned_data['lector'],
                libro = form.cleaned_data['libro'],
                devuelto = False,
                defaults= {
                    'fecha_prestamo':date.today()
                }  
            )
            return redirect('registrar_prestamo')
    else:
        form = PrestamoForm()
    #return
    return render(request,'lector/prestamoForm.html',{'form':form})

def addPrestamo_multiple(request):
    #
    if request.method == 'POST':
        form = PrestamoMultipleForm(request.POST)
        if form.is_valid():
            prestamos = []
            for l in form.cleaned_data['libros']:
                prestamo = Prestamo(
                    lector = form.cleaned_data['lector'],
                    libro = l,
                    fecha_prestamo = date.today(),
                    devuelto = False
                )
                prestamos.append(prestamo)
            #Bulk create o update toma una lista de objetos y los registra a todos
            Prestamo.objects.bulk_create(prestamos)
            return redirect('registrar_prestamo_m')
    else:
        form = PrestamoMultipleForm()
    #return
    return render(request,'lector/prestamoForm_m.html',{'form':form})