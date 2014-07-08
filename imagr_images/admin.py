from django.contrib import admin
from imagr_images.models import Photo, Album


class PhotoSizeFilter(admin.SimpleListFilter):
    title = "File Size"
    parameter_name = "image_size"

    def lookups(self, request, model_admin):
        return (
            ('0', "=< 1MB"),
            ('1', "1 MB < 10 MB"),
            ('2', "10MB < 100MB"),
            ('3', "> 100MB"),
        )

    def queryset(self, request, queryset):
        if self.value() == 'All':
            return queryset
        if self.value() == '0':
            return queryset.filter(image_size__lte=1048576)
        if self.value() == '1':
            return queryset.filter(
                image_size__lte=10485760, image_size__gt=1048576
            )
        if self.value() == '2':
            return queryset.filter(
                image_size__lte=104857600, image_size__gt=10485760
            )
        if self.value() == '3':
            return queryset.filter(
                image_size__lte=1048576000, image_size__gt=104857600
            )


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_modified')
    list_display = ('owner_link', 'title',)
    search_fields = (
        'owner__username', 'owner__first_name',
        'owner__last_name', 'owner__email'
    )


class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('date_uploaded', 'date_modified')
    list_display = ('owner_link', 'title', 'image_size', 'date_uploaded',)
    list_filter = ('date_uploaded', PhotoSizeFilter)
    search_fields = (
        'owner__username', 'owner__first_name',
        'owner__last_name', 'owner__email'
    )

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
