
from django.conf.urls import patterns, url


#from imagr_images import views

urlpatterns = patterns(
    'imagr_images.views',
    url(r'^$', "front_page", name='index'),
    url(r'^(?P<owner>\d+)/$', "home_page", name='home'),
    url(r'^album/(?P<album_id>\d+)$', "album_page", name='album'),
    url(r'^photo/(?P<photo_id>\d+)$', "photo_page", name='photo'),
    url(r'^stream/', "stream_page", name='stream'),
)
