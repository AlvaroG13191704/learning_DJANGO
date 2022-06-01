from django.urls import path
from .views import homePage,login_user
urlpatterns = [
    path('',homePage, name = 'home'),
    path('login/',login_user, name="is_login"),
]