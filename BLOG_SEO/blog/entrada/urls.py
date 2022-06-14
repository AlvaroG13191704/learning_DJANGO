from django.urls import path
from .views import EntryList,EntryDetailView
urlpatterns = [
    path('entradas/',EntryList, name = 'entry_lista'),
    path('entrada/<pk>',EntryDetailView.as_view(),name='detail_entry')
]