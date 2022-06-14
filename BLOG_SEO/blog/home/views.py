
from django.shortcuts import redirect, render
from home.forms import SuscribersForms,ContactForm
from home.models import Home
#models import
from entrada.models import Entry
# Create your views here.
def HomePageView(request):
    portada = Entry.objects.entrada_en_portada()
    entradas_home = Entry.objects.entradas_en_homes()
    entradas_recientes = Entry.objects.entradas_recientes()
    #charge model Home
    home = Home.objects.latest('created')
    #send email
    if request.method == 'POST':
        form = SuscribersForms(request.POST)
        form.save()
    else:
        form = SuscribersForms()
    return render(request,'home/index.html',{
        'portada':portada,
        'entradas_home':entradas_home,
        'entradas_recientes':entradas_recientes,
        'home':home,
        'form':form,
    })

def Contactform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
