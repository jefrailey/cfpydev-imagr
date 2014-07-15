from django.shortcuts import render
from django.http import HttpResponse as Response
from django.http import Http404
from imagr_images.models import Photo
from imagr_images.models import Album
# from easy_thumbnails.files import get_thumbnailer


# Create your views here.
def front_page(request):
    u"""shows anonymous users something nice to encourage them to sign up"""
    return render(request, 'imagr_images/index.html')


def home_page(request):
    u"""shows logged-in users a list of their albums, with a representative
    image from each album
    """
    if request.user.is_authenticated():
        albums = Album.objects.filter(owner=request.user)
        context = {'albums': albums}
        return render(request, 'imagr_images/home.html', context)
    else:
        return render(request, 'imagr_images/index.html')


def album_page(request, album_id):
    u"""shows logged-in users a display of photos in a single album"""
    try:
        album = Album.objects.get(pk=album_id, owner=request.user)
        photos = album.all_photos()
        title = album.title
        context = {'photos': photos, 'title': title}
        return render(request, 'imagr_images/album.html', context)
    except Exception:
        return render(request, 'imagr_images/our_404.html')


def photo_page(request, photo_id):
    u"""shows logged-in users a single photo along with details about it."""
    try:
        photo = Photo.objects.get(pk=photo_id)
        context = {'photo': photo}
        return render(request, 'imagr_images/photo.html', context)
    except Exception:
        return render(request, 'imagr_images/our_404.html')


def stream_page(request):
    u"""shows users their most recent photos along with recent photos uploaded
    by friends or those they are following.
    """
    photos = request.user.stream_photos()

    context = {'owner': request.user, 'photos': photos}

    return render(request, 'imagr_images/stream.html', context)
