from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^imagr_images/', include('imagr_images.urls', namespace='imagr_images')),
    url(r'^imagr_users/', include('imagr_users.urls', namespace='imagr_users')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

