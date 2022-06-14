
from django.urls import path
from .views import HomePageView,Contactform
urlpatterns = [
    path('',HomePageView, name = 'home'),
    path('contact/',Contactform,name='contact')
]