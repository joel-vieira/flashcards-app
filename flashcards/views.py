from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Deck, Flashcard


def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "flashcards/dashboard.html")

class DecksIndexView(generic.ListView):
    template_name = "flashcards/decks.html"
    context_object_name = "decks"

    def get_queryset(self) -> QuerySet:
        return Deck.objects.all()


class FlashcardsIndexView(generic.ListView):
    template_name = "flashcards/flashcards.html"
    context_object_name = "flashcards"

    def get_queryset(self) -> QuerySet:
        deck_id = self.kwargs.get('deck_id')
        return Flashcard.objects.filter(deck__id=deck_id)


class FlashcardDetailView(generic.DetailView):
    model = Flashcard
    template_name = "flashcards/flashcard_detail.html"
