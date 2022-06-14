from .models import Category, Entry
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.generic import DetailView
# Create your views here.
def EntryList(request):
    #kword = request.GET.get('kword','')
    kword = request.GET.get('kword','')
    categoria = request.GET.get('categoria','')
    categorias = Category.objects.all()
    entradas = Entry.objects.buscar_entrada(kword,categoria)
    #paginator = Paginator(resultado,10)
    print(kword)
    return render(request,'entrada/lista.html',{'entradas':entradas,'categorias':categorias})


class EntryDetailView(DetailView):
    model = Entry
    template_name = "entrada/detail.html"
