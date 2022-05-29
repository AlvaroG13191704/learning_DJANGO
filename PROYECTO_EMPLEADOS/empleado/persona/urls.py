from django.urls import path
from persona.views import ListaEmpleadosByArea, listaEmpleadosAdmin, EmpleadoUpdateView,EmpleadoDeleteView,EmpleadoCreateView
from persona.views import listaEmpleados
from persona.views import verEmpleado

urlpatterns = [
    path('lista/', listaEmpleados.as_view(), name='lista_empleados'),
    path('empleado/<int:id>',verEmpleado, name = 'empleado'),
    path('lista/area/<shorname>', ListaEmpleadosByArea.as_view(), name='empleados_area'),
    path('lista/empleados/admin', listaEmpleadosAdmin.as_view(), name='empleados_admin'),

    #CRUD
    path('add/', EmpleadoCreateView.as_view(), name='empleado_add'),
    path('update/empleado/<pk>',EmpleadoUpdateView.as_view(),name="update_empleado"),
    path('delete/empleado/<pk>/', EmpleadoDeleteView, name='delete_empleado'),
]