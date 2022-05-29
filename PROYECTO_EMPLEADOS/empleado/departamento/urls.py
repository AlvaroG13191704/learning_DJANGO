from django.urls import path
from departamento.views import newDepaView, DepartamentoListView

urlpatterns = [
    path('lista/', DepartamentoListView.as_view(), name='listaDepa'),
    path('new/',newDepaView.as_view(),name='new_department'),
]