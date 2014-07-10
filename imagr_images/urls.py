from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

from imagr_images import views

urlpatterns = patterns(
    '',
    url(r'^index/', views.front_page, name='index'),
    url(r'^(?P<owner>\d+)/$', views.home_page, name='home'),
    url(r'^(?P<owner_id>\d+)/album/(?P<album_id>\d+)$', views.album_page, name='album'),
    url(r'^(?P<owner_id>\d+)/photo/(?P<photo_title>\d+)$', views.photo_page, name='photo'),
    url(r'^(?P<owner_id>\d+)/stream/', views.stream_page, name='stream'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
