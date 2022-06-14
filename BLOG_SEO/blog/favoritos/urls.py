
from django.urls import path
from favoritos import views
urlpatterns = [
    path('perfil/',views.UserPageListView, name = 'perfil'),
    path('add_entrada/<pk>/',views.AddFavoritosView.as_view(),name='add_entrada'),
    path('delete_favorites/<pk>/',views.FavoritosDeleteView.as_view(),name='delete_favoritos'),

]