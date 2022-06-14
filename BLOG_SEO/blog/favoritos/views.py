from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import Favorites
from entrada.models import Entry
from django.views.generic import ListView,View,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
#
@login_required(login_url='login_user')
def UserPageListView(request):
    entradas_user = Favorites.objects.entradas_user(request.user)
    return render(request,'favoritos/perfil.html',{'entradas_user':entradas_user})

class AddFavoritosView(LoginRequiredMixin ,View):
    login_url = reverse_lazy('login_user')
    def post(self,request,*args,**kwards):
        #Get user
        user = self.request.user
        entrada = Entry.objects.get(id=self.kwargs['pk'])
        #register
        Favorites.objects.create(
            user = user,
            entry = entrada,
        )
        return HttpResponseRedirect(
            reverse(
                'perfil'
            )
        )

class FavoritosDeleteView(DeleteView):
    model = Favorites 
    success_url = '/'
