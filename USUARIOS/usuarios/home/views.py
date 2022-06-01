from django.shortcuts import render
from django.contrib.auth.decorators import login_required
"""
Con login_required es como usar mixin con clases pero este decorador hace más facil todo
ya que se le agrega al inicio de la funcion y si ve que no esta con sesión iniciada entonces no lo dejara entrar 
"""
# Create your views here.
def homePage(request):
    return render(request,'home/index.html')

"""
Con LOGIN_URL le mandamos el name de nuestra URL que queremos que vaya si no esta logeado
"""
@login_required(login_url='login_user')
def login_user(request):
    return render(request,'home/index2.html')