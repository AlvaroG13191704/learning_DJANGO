from django.urls import path
from .views import EntryList,EntryDetailView
urlpatterns = [
    path('entradas/',EntryList, name = 'entry_lista'),
    path('entrada/<slug>',EntryDetailView.as_view(),name='detail_entry')
]