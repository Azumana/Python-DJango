from django.db import models

# Create your models here.

ARTISTS = {
    'nekfeu': {'name': 'Nekfeu'},
    'disiz': {'name': 'Disiz'},
    'shaka ponk': {'name': 'Shaka Ponk'},
}

ALBUMS = [
    {'name': 'Les Etoiles Vagabondes', 'artists': [ARTISTS['nekfeu']]},
    {'name': 'Disizila', 'artists': [ARTISTS['disiz']]},
    {'name': 'Apelogies', 'artists': [ARTISTS['shaka ponk']]}
]