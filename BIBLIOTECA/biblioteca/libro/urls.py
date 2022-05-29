from django.urls import path
from .views import listaLibros,listaLibros2,ver_libro

urlpatterns = [
    path('lista/',listaLibros, name="lista_libro"),
    path('lista/categoria/',listaLibros2, name="lista_categoria"),
    path('lista/ver/libro/<int:id>/',ver_libro,name='ver_libro')
]