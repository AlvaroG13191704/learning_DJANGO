
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import ListView
from departamento.forms import newDepartamentoForm

from persona.models import Empleado
from departamento.models import Departamento
# Create your views here.

class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = "departamentos"


class newDepaView(FormView):
    template_name = 'departamento/new_depa.html'
    form_class = newDepartamentoForm
    success_url = reverse_lazy('listaDepa')

    def form_valid(self, form):

        depa = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name']
        )
        depa.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento=depa,
        )
        return super(newDepartamentoForm,self).form_valid(form)