from django.contrib import admin
from django import forms
from .models import Card,Usuario,Token,Deck,DeckCard

class CardAdmin(admin.ModelAdmin):
    list_filter = ["name"]
    search_fields = ["name"]


class DeckCardAdmin(admin.ModelAdmin):
    autocomplete_fields = ['card']
    search_fields = ['card__name']

# Register your models here.
admin.site.register(Card,CardAdmin)
admin.site.register(Usuario)
admin.site.register(Token)
admin.site.register(Deck)
admin.site.register(DeckCard,DeckCardAdmin)