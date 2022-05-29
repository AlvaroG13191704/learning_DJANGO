from django.shortcuts import render

#Models import
from .models import Autor
# Create your views here.
def listaAutores(request):
    kword = request.GET.get('kword','')
    print(kword)
    autores = Autor.objects.buscar_autor_edad()
    return render(request,'autor/lista.html',{'autores':autores})