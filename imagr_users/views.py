from django.shortcuts import render
from django.http import HttpResponse as Response
from imagr_images.models import Photo
from imagr_images.models import Album


def stream_page(request):
    u"""shows users their most recent photos along with recent photos uploaded
    by friends or those they are following.
    """
    photos = request.user.stream_photos()

    context = {'owner': request.user, 'photos': photos}

    return render(request, 'imagr_images/stream.html', context)
