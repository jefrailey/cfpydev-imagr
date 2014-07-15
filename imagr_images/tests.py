from django.test import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from django.template.defaultfilters import escape
from django.conf import settings
from imagr_images.models import Photo, Album
from imagr_users.models import ImagrUser
from django.core.files import File
import os


class ImagesTests(TestCase):
    def setUp(self):
        u"""Create a user and image that can be used in all tests.
        Create a temp folder for images to be stored in, so test images
        don't clog up regular media folder."""

        TEST_ROOT = os.path.abspath(os.path.dirname(__file__))

        self._old_MEDIA_ROOT = settings.MEDIA_ROOT
        # override MEDIA_ROOT for this test
        settings.MEDIA_ROOT = os.path.join(TEST_ROOT, 'test_data/media/')

        self.DJANGO_CONFIGURATION = 'Test'

        user = ImagrUser(username="tester")
        user.save()

        test_dir = os.listdir(os.getcwd() + "/test_data/test_pics")
        test_dir = \
            [os.getcwd() + "/test_data/test_pics/" + name for name in test_dir]

        test_albums = [u"Tester's Album", u"Tester's Second Album"]

        for pic in test_dir:
            with open(pic, 'r') as file_:
                a_photo = File(file_)
                photo = Photo()
                photo.image = a_photo
                photo.owner = user
                photo.published = 1
                photo.save()

        for test_album in test_albums:
            album = Album()
            album.title = test_album
            album.owner = user
            album.published = 1
            album.save()

        self.generator = self._name_generator()

    def tearDown(self):
        # reset MEDIA_ROOT
        settings.MEDIA_ROOT = self._old_MEDIA_ROOT

    def test_save(self):
        u"""Photo test"""
        for photo in Photo.objects.all():
            self.assertGreater(photo.image_size, 0)

    def test_owner_link(self):
        u"""Owner link test"""
        for photo in Photo.objects.all():
            self.assertEqual(photo.owner_link(), '<a href="%s">%s</a>' % (reverse(
            "admin:imagr_users_imagruser_change", args=(photo.owner.id,)), escape(photo.owner)
        ))

    def test_album_has_no_photos(self):
        u"""Album test"""
        album = self._create_album()
        self.assertFalse(album.photos.all().exists())

    def test_album_has_one_photo(self):
        u"""Album test"""
        album = self._create_album()
        photo = Photo.objects.all()[0]
        album.photos.add(photo)
        self.assertEquals(album.photos.get(pk=photo.pk), photo)

    def test_album_has_multiple_photos(self):
        u"""Album test"""
        album = self._create_album()
        self._add_all_photos_to_album(album)
        for photo in Photo.objects.all():
            self.assertIn(photo, album.photos.all())

    def test_cover_photo_exits(self):
        u"""Album test"""
        album = self._create_album()
        photo = Photo.objects.all()[0]
        album.photos.add(photo)
        self._add_cover_photo(photo, album)
        self.assertEquals(album.cover_photo.all()[0], photo)

    def test_cover_function_returns_cover_photo(self):
        album = self._create_album()
        photo = Photo.objects.all()[0]
        album.photos.add(photo)
        self._add_cover_photo(photo, album)
        self.assertEquals(album.cover(), photo)

    def test_all_photos_returns_all_photos(self):
        album = self._create_album()
        self._add_all_photos_to_album(album)
        for photo in album.photos.all():
            self.assertIn(photo, album.all_photos())

    def _add_all_photos_to_album(self, album):
        for photo in Photo.objects.all():
            album.photos.add(photo)

    def _add_cover_photo(self, photo, album):
        album.cover_photo.add(photo)

    def _create_album(self):
        album = Album(
            title=self.generator,
            owner=ImagrUser.objects.all()[0],
            published=1
            )
        album.save()
        return album

    def _name_generator(self):
        names = [chr(n) for n in xrange(97, 123)]
        for name in names:
            yield name