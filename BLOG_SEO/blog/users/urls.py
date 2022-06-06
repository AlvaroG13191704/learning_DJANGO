
from django.urls import path
from .views import user_register,login_user,logout_user,update_password
urlpatterns = [
    path('register/',user_register, name = 'register_user'),
    path('login/',login_user, name = 'login_user'),
    path('logout/',logout_user,name="logout_user"),
    path('update/password/',update_password, name="update_pass"),
]