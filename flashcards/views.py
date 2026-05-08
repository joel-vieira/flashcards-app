from django.db.models.query import QuerySet
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Deck, Flashcard


def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'flashcards/dashboard.html')


class DecksIndexView(generic.ListView):
    template_name = 'flashcards/decks.html'
    context_object_name = 'decks'

    def get_queryset(self) -> QuerySet:
        return Deck.objects.all()


class FlashcardsIndexView(generic.ListView):
    template_name = 'flashcards/flashcards.html'
    context_object_name = 'flashcards'

    def get_queryset(self) -> QuerySet:
        deck_id = self.kwargs.get('deck_id')
        if not Deck.objects.filter(pk=deck_id).exists():
            raise Http404('Object not found')

        return Flashcard.objects.filter(deck__id=deck_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deck'] = Deck.objects.get(pk=self.kwargs.get('deck_id'))
        return context


class FlashcardDetailView(generic.DetailView):
    model = Flashcard
    template_name = 'flashcards/flashcard_detail.html'

    def get_object(self):
        return get_object_or_404(Flashcard, pk=self.kwargs.get('pk'), deck__id=self.kwargs.get('deck_id'))
