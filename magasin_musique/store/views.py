#from django.shortcuts import render
from django.http import HttpResponse

from .models import ALBUMS

def index(request):
    message ="Youpi t'es pas trop débile t'as réussis NOOB"
    return HttpResponse(message)


def listing(request):
    albums= ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)


def detail(request, album_id):
    id = int(album_id)
    album = ALBUMS[id]
    artists = "".join([artist['name']for artist in album])
    message = " le nom de l'album est {}. Il a été écrit par {}".format(album['name'], artists)
    return HttpResponse(message)