from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from personas.models import Persona

# Create your views here.
def home(request):
    #Integrar la info de la clase de modelo
    """
    Con objects nos conectamos a la base de datos
    """
    no_personas = Persona.objects.count()
    #personas = Persona.objects.all() #Query para traer todos los tipo persona
    personas = Persona.objects.order_by('id')
    respuesta = {
        'nopersonas': no_personas,
        'personas': personas,
    }
    return render(request,'bienvenido.html',respuesta)
