from django.test import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from django.template.defaultfilters import escape
from django.conf import settings
from imagr_images.models import Photo, Album
from imagr_users.models import ImagrUser, Relationship
from django.core.files import File
import os


class UserTests(TestCase):
    def setUp(self):
        u"""Create a name generator"""
        self.generator = self._name_generator()

    def test_user_creation(self):
        user = ImagrUser(username=self.generator.next())
        user.save()
        self.assertTrue(ImagrUser.objects.all().exists())

    def test_follow(self):
        user = ImagrUser(username=self.generator.next())
        other = ImagrUser(username=self.generator.next())
        user.save()
        other.save()
        self.assertFalse(Relationship.objects.all().exists())
        user.follow(other)
        self.assertTrue(Relationship.objects.all().exists())

    def test_unfollow(self):
        user = ImagrUser(username=self.generator.next())
        other = ImagrUser(username=self.generator.next())
        user.save()
        other.save()
        user.follow(other)
        self.assertTrue(Relationship.objects.all().exists())
        user.unfollow(other)
        self.assertFalse(Relationship.objects.all().exists())

    def _name_generator(self):
        names = [chr(n) for n in xrange(97, 123)]
        for name in names:
            yield name