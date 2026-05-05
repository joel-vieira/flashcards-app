from django.db import models


class Deck(models.Model):
    name = models.CharField("Name", max_length=50)

    def __str__(self):
        return self.name


class Flashcard(models.Model):
    # Front
    front_text = models.CharField("Front Text", max_length=70)
    comment = models.CharField("Comment", max_length=120, blank=True, null=True)
    # Back
    back_text = models.CharField("Back Text", max_length=70)
    reading = models.CharField("Reading", max_length=70, blank=True, null=True)
    explanation = models.TextField("Explanation", blank=True, null=True)
    example_text = models.TextField("Example Text", blank=True, null=True)
    # Relations
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    # Metadata
    created_at = models.DateTimeField("Creation Datetime", auto_now_add=True)
    modified_at = models.DateTimeField("Modification Datetime", auto_now=True)

    def __str__(self):
        return self.front_text
