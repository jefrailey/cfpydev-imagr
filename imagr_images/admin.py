from django.contrib import admin
from imagr_images.models import Photo, Album


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_modified')
    list_display = ('owner', 'title')
    search_fields = (
        'owner__username', 'owner__first_name',
        'owner__last_name', 'owner__email'
    )


class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('date_uploaded', 'date_modified')
    list_display = ('owner', 'title', 'image_size', 'date_uploaded')
    list_filter = ('date_uploaded',)
    search_fields = (
        'owner__username', 'owner__first_name',
        'owner__last_name', 'owner__email'
    )

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
