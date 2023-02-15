from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.template import loader
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from deckbuilder.models import Card,Deck,DeckCard,Usuario,Token
from django.views.generic import ListView
from django.http import JsonResponse


def index(request):
    #ORM pintar cartas
    cartas = Card.objects.order_by('cardnumber')
    template = loader.get_template('deckbuilder/index.html')
    paginator = Paginator(cartas, 12)
    page = request.GET.get('page')
    expansiones = Card.objects.values_list('set_name').distinct()
    datos = [field.name for field in Card._meta.get_fields() if field.name not in ['deck', 'deckcard','card_sets','image_url','maineffect','sourceeffect']]
    

    try:
        cartas = paginator.page(page)
    except PageNotAnInteger:
        cartas = paginator.page(1)
    except EmptyPage:
        cartas = paginator.page(paginator.num_pages)
        template = loader.get_template('deckbuilder/index.html')
    return render(request,'deckbuilder/index.html',{
        'cartas':cartas,
        'expansiones':expansiones,
        'datos' : datos,
    })
    

def search(request):
    if request.method == "POST":
        input = request.POST.get("input")
        results = Card.objects.filter(name__contains=input)
        data = {
            'results': [{'id': card.id, 'name': card.name} for card in results]
        }
        return JsonResponse(data)
    return render(request,'busqueda.html')

def decks(request):
    decks = Deck.objects.all()[:5]
    return render(request,'deckbuilder/decks.html',{
        'decks':decks,
    })
def decklist(request,):

    deckcards = DeckCard.objects.filter(deck__name=Deck.name)
    return render(request, 'deckbuilder/decklist.html', {
        'carta': deckcards
    })