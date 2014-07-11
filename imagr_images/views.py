from django.shortcuts import render
from django.http import HttpResponse as Response
from imagr_images.models import Photo
from imagr_images.models import Album
# from easy_thumbnails.files import get_thumbnailer


# Create your views here.
def front_page(request):
    u"""shows anonymous users something nice to encourage them to sign up"""
    return Response('You want to share with us. Sign up now!')


def home_page(request, owner):
    u"""shows logged-in users a list of their albums, with a representative
    image from each album
    """
    if request.user.is_authenticated():
        albums = Album.objects.filter(owner=request.user)
        context = {'owner': owner, 'albums': albums}
        return render(request, 'imagr_images/home.html', context)


def album_page(request, album_id):
    u"""shows logged-in users a display of photos in a single album"""
    album = Album.objects.get(pk=album_id, owner=request.user)
    photos = album.all_photos()
    title = album.title
    context = {'photos': photos, 'title': title}
    return render(request, 'imagr_images/album.html', context)


def photo_page(request, photo_id):
    u"""shows logged-in users a single photo along with details about it."""
    photo = Photo.objects.get(pk=photo_id)
    context = {'photo': photo}
    return render(request, 'imagr_images/photo.html', context)
