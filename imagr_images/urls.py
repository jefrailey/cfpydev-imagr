from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

#from imagr_images import views

urlpatterns = patterns(
    'imagr_images.views',
    url(r'^index/', "front_page", name='index'),
    url(r'^(?P<owner>\d+)/$', "home_page", name='home'),
    url(r'^(?P<owner_id>\d+)/album/(?P<album_id>\d+)$', "album_page", name='album'),
    url(r'^(?P<owner_id>\d+)/photo/(?P<photo_title>\d+)$', "photo_page", name='photo'),
    url(r'^(?P<owner_id>\d+)/stream/', "stream_page", name='stream'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
