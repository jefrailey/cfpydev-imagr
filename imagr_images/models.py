import datetime
from django.conf import settings
from django.template.defaultfilters import escape
from django.core.urlresolvers import reverse
from django.db import models
import os.path

PRIVACY_LEVELS = (
    (0, 'Private'),
    (1, 'Public'),
)


def get_file_owner_username(instance, filename):
    "Calculate a storage path for this file instance"
    parts = [instance.owner.username]
    today = datetime.datetime.utcnow()
    parts.extend(map(unicode, [today.year, today.month]))
    parts.append(os.path.basename(filename))
    path = u"/".join(parts)
    return path


class Photo(models.Model):
    """Represent a single photo in a collection of photos
    """
    image = models.ImageField(
        upload_to=get_file_owner_username,
        height_field='height',
        width_field='width',
    )
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    height = models.PositiveSmallIntegerField(default=0, editable=False)
    width = models.PositiveSmallIntegerField(default=0, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    published = models.IntegerField(choices=PRIVACY_LEVELS)
    image_size = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
        return self.title

    def published_between(self, start, end):
        return end <= self.date_uploaded <= start

    published_between.admin_order_field = 'published_between'
    published_between.boolean = True
    published_between.short_description = 'Published in selected range'

    def owner_link(self):
        return '<a href="%s">%s</a>' % (reverse(
            "admin:imagr_users_imagruser_change", args=(self.owner.id,)), escape(self.owner)
        )

    owner_link.allow_tags = True
    owner_link.short_description = "owner"

    def save(self, *args, **kwargs):
        self.image_size = self.image.size
        super(Photo, self).save(*args, **kwargs)


class Album(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    photos = models.ManyToManyField(
        Photo,
        related_name="albums",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    published = models.IntegerField(choices=PRIVACY_LEVELS)
    cover_photo = models.ManyToManyField(
        Photo,
        related_name="cover_of",
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.title

    def owner_link(self):
        return '<a href="%s">%s</a>' % (reverse(
            "admin:imagr_users_imagruser_change", args=(self.owner.id,)), escape(self.owner)
        )

    owner_link.allow_tags = True
    owner_link.short_description = "owner"

    def cover(self):
        try:
            _cover = self.cover_photo.all()[0]
            return _cover
        except IndexError:
            return None

    def all_photos(self):
        try:
            _all_photos = self.photos.all()
            print _all_photos
            return _all_photos
        except IndexError:
            return None
