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

    def tearDown(self):
        # reset MEDIA_ROOT
        settings.MEDIA_ROOT = self._old_MEDIA_ROOT

    # def test_published_between_true(self):
    #     u"""Photo test"""
    #     photo = Photo.objects.all()[0]
    #     self.assertEqual(photo.published_between(, False)

    def test_save(self):
        u"""Photo test"""
        for photo in Photo.objects.all():
            self.assertGreater(photo.image_size, 0)

    def test_owner_link(self):
        u"""Album test"""
        for photo in Photo.objects.all():
            self.assertEqual(photo.owner_link(), '<a href="%s">%s</a>' % (reverse(
            "admin:imagr_users_imagruser_change", args=(photo.owner.id,)), escape(photo.owner)
        ))

    # def test_cover(self):
    #     u"""Album test"""
    #     pass

    # def test_all_photos(self):
    #     u"""Album test"""
    #     pass
