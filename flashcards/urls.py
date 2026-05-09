from django.views.generic.base import RedirectView
from django.urls import path

from . import views

app_name = 'flashcards'

urlpatterns = [
    path('', RedirectView.as_view(url='dashboard/', permanent=False)),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('decks/', views.DecksIndexView.as_view(), name='decks'),
    path('decks/<int:deck_id>/', views.FlashcardsIndexView.as_view(), name='flashcards'),
    path('decks/<int:deck_id>/flashcards/<int:pk>', views.FlashcardDetailView.as_view(), name='flashcard'),
]
