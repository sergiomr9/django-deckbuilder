# django-deckbuilder


url = "https://digimoncard.io/api-public/search.php?series=Digimon Card Game"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            card = Card(
                name=item.get('name'),
                type=item.get('type'),
                color=item.get('color'),
                stage=item.get('stage'),
                digi_type=item.get('digi_type'),
                attribute=item.get('attribute'),
                level=item.get('level'),
                play_cost=item.get('play_cost'),
                evolution_cost=item.get('evolution_cost'),
                cardrarity=item.get('cardrarity'),
                artist=item.get('artist'),
                dp=item.get('dp'),
                cardnumber=item.get('cardnumber'),
                maineffect=item.get('maineffect'),
                sourceeffect=item.get('soureeffect'),
                set_name=item.get('set_name'),
                card_sets=item.get('card_sets'),
                image_url=item.get('image_url'),
            )
            card.save()
    else:
        # handle error
        return HttpResponse("Error while fetching data from API")
    return HttpResponse(response.text)