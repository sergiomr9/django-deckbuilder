from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.template import loader
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from deckbuilder.models import Card, Deck, DeckCard, Usuario, Token
from django.views.generic import ListView
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django import forms


def index(request):
    # ORM pintar cartas
    cartas = Card.objects.order_by('cardnumber')
    template = loader.get_template('deckbuilder/index.html')
    paginator = Paginator(cartas, 12)
    page = request.GET.get('page')
    expansiones = Card.objects.values_list('set_name').distinct()
    datos = [field.name for field in Card._meta.get_fields() if field.name not in [
        'deck', 'deckcard', 'card_sets', 'image_url', 'maineffect', 'sourceeffect']]

    try:
        cartas = paginator.page(page)
    except PageNotAnInteger:
        cartas = paginator.page(1)
    except EmptyPage:
        cartas = paginator.page(paginator.num_pages)
        template = loader.get_template('deckbuilder/index.html')
    return render(request, 'deckbuilder/index.html', {
        'cartas': cartas,
        'expansiones': expansiones,
        'datos': datos,
    })


def search(request):
    if request.method == "POST":
        input = request.POST.get("input")
        results = Card.objects.filter(name__contains=input)
        data = {
            'results': [{'id': card.id, 'name': card.name} for card in results]
        }
        return JsonResponse(data)
    return render(request, 'busqueda.html')


def decks(request):
    decks = Deck.objects.all()[:5]
    return render(request, 'deckbuilder/decks.html', {
        'decks': decks,
    })


def decklist(request, pk):
    deck = Deck.objects.get(pk=pk)
    from django.db.models import F

    deckcards = deck.deckcard_set.all().order_by(
        F('card__level').asc(nulls_last=True))

    return render(request, 'deckbuilder/decklist.html', {
        'deckcards': deckcards,
        'deck': deck
    })


def detalle(request, cardnumber):
    carta = Card.objects.get(cardnumber=cardnumber)

    context = {
        'name': carta.name,
        'type': carta.type,
        'color': carta.color,
        'stage': carta.stage,
        'digi_type': carta.digi_type,
        'attribute': carta.attribute,
        'level': carta.level,
        'play_cost': carta.play_cost,
        'evolution_cost': carta.evolution_cost,
        'cardrarity': carta.cardrarity,
        'artist': carta.artist,
        'dp': carta.dp,
        'cardnumber': carta.cardnumber,
        'maineffect': carta.maineffect,
        'sourceeffect': carta.sourceeffect,
        'card_set': carta.card_sets,
        'image_url': carta.image_url,
    }
    return render(request, 'deckbuilder/detalle.html', {
        'context': context
    })


def create_deck(request):
    if request.method == 'POST':
       
        deck_cards = request.POST.getlist('deck_cards')
        deck_card_counts = request.POST.getlist('deck_card_counts')
        
        # Crear el deck
        deck = Deck.objects.create()
        
        # Añadir cartas al deck
        for i in range(len(deck_cards)):
            card = Card.objects.get(pk=deck_cards[i])
            deck_card_count = deck_card_counts[i]
            DeckCard.objects.create(card=card, deck=deck, count=deck_card_count)
        
        return redirect('deck_detail', deck.pk)
    else:
        cards = Card.objects.all()
        return render(request, 'deckbuilder/builder.html', {'cards': cards})
        