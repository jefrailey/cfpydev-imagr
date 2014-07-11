from django.conf.urls import patterns, url


urlpatterns = patterns(
    'imagr_users.views',
    url(r'^stream/', "stream_page", name='stream'),
)
