from django.conf.urls import patterns, url

from imagr_images import views

urlpatterns = patterns(
    '',
    url(r'^index/', views.front_page, name='index'),
    url(r'^(?P<owner>\d+)/$', views.home_page, name='home'),
    url(r'^(?P<owner_id>\d+)/album/(?P<album_title>\d+)$', views.album_page, name='album'),
    url(r'^(?P<owner_id>\d+)/photo/(?P<photo_title>\d+)$', views.photo_page, name='photo'),
    url(r'^(?P<owner_id>\d+)/stream/', views.stream_page, name='stream'),
)
