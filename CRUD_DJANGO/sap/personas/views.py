from xml import dom
from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView
from personas.models import Persona, Domicilio
from personas.forms import PersonaForm
from personas.forms2 import DomicilioForm
from django.urls import reverse_lazy, reverse

#Search user
def searchUser(request):
    if request.method == 'POST':
        name = request.POST['kword']
        persona = Persona.objects.filter(nombre=name)
        print(persona)
        return render(request,'search.html',{'personas':persona})
    else:
        return render(request,'search.html')

#CreateView
class newPersonCW(CreateView):
    #Refert to the template
    template_name = 'formsCW.html'
    #Reference to the model
    model = Persona
    #The fields that we want to field->could be
    fields = ('__all__')
    #fields = ['nombre','apellido','email','domicilio']
    succes_url = reverse_lazy('inicio') #->Problem

# Create your views here.
def detallePersona(request,id):
    #Con get especificamos una llave primaria pk -> primary key
    #persona = Persona.objects.get(pk=id) 
    #Este hace lo mismo pero nos redirije a la pagina no encontrada
    persona = get_object_or_404(Persona, pk=id)
    respuesta = {
        'persona': persona,
    }
    return render(request,'detalle.html',respuesta)

#Indica la clase de persona que vamos a utilizar
"""
Para que no tire error en modelform hay que excluir
"""
#PersonaForm = modelform_factory(Persona,exclude=[])

def nuevaPersona(request):
    #Formato de clase que trae django para agregar una persona
    if request.method == 'POST':
        #Guardar la inf en base de datos
        #En request esta toda la inf
        formaPersona = PersonaForm(request.POST)
        #Validar el forms
        if formaPersona.is_valid:
            #Guardar la inf
            formaPersona.save()
            return redirect('inicio')
    else:
        #Nueva clase
        formaPersona = PersonaForm()
    return render(request,'nuevo.html',{'formaPersona':formaPersona})

def editarPersona(request,id):
    #Con esto instanceamos para obtener el id persona
    persona = get_object_or_404(Persona,pk=id)
    #Evaluamos cuando sea tipo POST
    if request.method == 'POST':
        #Recuperamos la inf del post
        formaPersona = PersonaForm(request.POST,instance=persona)
        #Validar el forms
        if formaPersona.is_valid:
            #Guardar la inf
            formaPersona.save()
            return redirect('inicio')
    else:
        #Esto es posible xp adentro de la clase persona indicamos el modelo Persona
        formaPersona = PersonaForm(instance=persona)
    return render(request,'editar.html',{'formaPersona':formaPersona})

def eliminarPersona(request,id):
    #Con esto instanceamos para obtener el id persona
    persona = get_object_or_404(Persona,pk=id)
    #Vemos que exista el id
    if persona:
        #Lo eliminamos
        persona.delete()
    return redirect('inicio')

#######################################
#Mostrar los domicilios
def mostrarDomicilios(request):
    #Traer todos los domicilios
    domicilios = Domicilio.objects.order_by('id')
    return render(request,'detalleDomi.html',{'domicilios':domicilios})

#Agregar persona
def nuevoDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid:
            formaDomicilio.save()
            return redirect('domi')
    else:
        formaDomicilio = DomicilioForm()
    return render(request,'dominuevo.html',{'formaDomicilio':formaDomicilio})

#Mostrar detalle
def detalleDomicilio(request,id):
    #Traemos el id con su pk
    domicilio = get_object_or_404(Domicilio,pk = id)
    return render(request,'domidetalle.html',{'domicilio':domicilio})

#Editar domi
def editarDomicilio(request,id):
    #Traemos el id 
    domicilio = get_object_or_404(Domicilio, pk = id)
    #Validamos
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio)
        if formaDomicilio.is_valid:
            formaDomicilio.save()
            return redirect('domi')
    else:
        formaDomicilio = DomicilioForm(instance=domicilio)
    return render(request, 'editardomi.html',{'formaDomicilio':formaDomicilio})

#Eliminar domi
def eliminarDomicilio(request,id):
    domicilio = get_object_or_404(Domicilio,pk = id)
    if domicilio:
        domicilio.delete()
    return redirect('domi')