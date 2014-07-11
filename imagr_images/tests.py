from django.test import TestCase
from django.test.client import RequestFactory
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

        with open("test_images/1.png", 'rb') as file_:
            a_photo = File(file_)
            photo = Photo(title=u"Tester's Photo", image=a_photo,
                          privacy=0, owner=user)
            photo.save()

        with open("test_images/2.png", 'rb') as file_:
            a_photo = File(file_)
            photo = Photo(title=u"Tester's Second Photo", image=a_photo,
                          privacy=0, owner=user)
            photo.save()

        album = Album(title="Tester's Album", privacy=0, owner=user)
        album.save()
        album2 = Album(title="Tester's Second Album", privacy=0, owner=user)
        album2.save()

    def tearDown(self):
        # reset MEDIA_ROOT
        settings.MEDIA_ROOT = self._old_MEDIA_ROOT

    # def test_published_between_true(self):
    #     u"""Photo test"""
    #     photo = Photo.objects.all()[0]
    #     self.assertEqual(photo.published_between(, False)

    def test_save(self):
        u"""Photo test"""
        photo = Photo.objects.all()[0]
        self.assertGreater(photo, 0)

    def test_owner_link(self):
        u"""Album test"""
        pass

    def test_cover(self):
        u"""Album test"""
        pass

    def test_all_photos(self):
        u"""Album test"""
        pass
