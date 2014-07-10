from django.shortcuts import render
from django.http import HttpResponse as Response
from imagr_images.models import Photo
from imagr_images.models import Album


# Create your views here.
def front_page(request):
    u"""shows anonymous users something nice to encourage them to sign up"""
    return Response('You want to share with us. Sign up now!')


def home_page(request, owner):
    u"""shows logged-in users a list of their albums, with a representative
    image from each album
    """
    if request.user.is_authenticated():
        albums = Album.objects.filter(owner=request.user.id)
        context = {'albums': albums}
        return render(request, 'imagr_images/home.html', context)

# def _get_owner_album(owner_id):
#     return Album.objects.filter(owner=owner_id)


def album_page(request, album_id, owner_id):
    u"""shows logged-in users a display of photos in a single album"""
    album = Album.objects.get(pk=album_id)
    photos = album.all_photos()
    title = album.title
    context = {'photos': photos, 'title': title}
    return render(request, 'imagr_images/album.html', context)


def photo_page():
    u"""shows logged-in users a single photo along with details about it."""
    pass


def stream_page():
    u"""shows users their most recent photos along with recent photos uploaded
    by friends or those they are following.
    """
    pass
