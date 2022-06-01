from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserLoginForm,UpdatePasswordForm
from django.contrib.auth import authenticate,login,logout
from .models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
#Crear usuario
def user_register(request):
    if request.method == 'POST':
        #Traer el form
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(   
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password1'],
                nombres = form.cleaned_data['nombres'],
                apellidos = form.cleaned_data['apellidos'],
                genero = form.cleaned_data['genero']
            )
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{"form":form})
#Login
def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request,user)
                return redirect('is_login')
    else:
        form = UserLoginForm()
    return render(request,'users/login.html',{"form":form})

#logout user
@login_required(login_url='login_user')
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')


#Cambiar contraseña
@login_required(login_url='login_user')
def update_password(request):
    if request.method == 'POST':
        #Traer el form
        form = UpdatePasswordForm(request.POST)
        if form.is_valid():
            usuario = User.objects.get(username=request.user.username)
            user = authenticate(
                username = usuario.username,
                password = form.cleaned_data['password'],
            )
            if user:
                new_pass = form.cleaned_data['password_new']
                usuario.set_password(new_pass)
                usuario.save()
            logout(request)
            return redirect('login_user')
    else:
        form = UpdatePasswordForm()
    return render(request,'users/update.html',{"form":form})