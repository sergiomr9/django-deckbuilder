from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, unique=True, null=False)
    passwd = models.CharField(max_length=255, null=False)
    img = models.CharField(max_length=255, null=True, blank=True)
    correo = models.EmailField(unique=True, null=False)
    descripcion = models.TextField(null=True, blank=True)


class Token(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    valor = models.CharField(max_length=255)
    expiracion = models.DateTimeField(auto_now_add=True)


class Card(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255,null=True)
    color = models.CharField(max_length=255)
    stage = models.CharField(max_length=255,null=True)
    digi_type = models.CharField(max_length=255, null=True)
    attribute = models.CharField(max_length=255, null=True)
    level = models.IntegerField(null=True)
    play_cost = models.IntegerField(null=True)
    evolution_cost = models.IntegerField(null=True)
    cardrarity = models.CharField(max_length=255,null=True)
    artist = models.CharField(max_length=255, null=True)
    dp = models.IntegerField(null=True,blank=True)
    cardnumber = models.CharField(max_length=255, primary_key=True)
    maineffect = models.TextField(null=True, blank=True)
    sourceeffect = models.TextField(null=True, blank=True)
    set_name = models.CharField(max_length=255)
    card_sets = models.TextField()
    image_url = models.URLField()
    def __str__(self):
        return f"{self.name} {self.cardnumber}"

class Deck(models.Model):
    
    name = models.CharField(max_length=255)
    cards = models.ManyToManyField(Card, through='DeckCard')
    image = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.name
    

class DeckCard(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField()

    def save(self, *args, **kwargs):
        maineffect = self.card.maineffect
        if self.card.maineffect is None:
            maineffect = ""
        if "You can include up to 50 copies of cards with this card's card number in your deck." in maineffect:
            max_count = 50
            
        else:
            max_count = 4

        if self.count > max_count:
            raise ValueError(f"The maximum number of copies for this card is {max_count}")

        if DeckCard.objects.filter(card=self.card, deck=self.deck).count() + self.count > 55:
            raise ValueError("The maximum number of cards in the deck is 55")

        super(DeckCard, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.card} {self.deck} {self.count}"


    