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
        user, other = self.create_followers()
        user.unfollow(other)
        self.assertEqual(Relationship.objects.all()[0].follower_status, 0)

    def test_request_friendship(self):
        user = ImagrUser(username=self.generator.next())
        other = ImagrUser(username=self.generator.next())
        user.save()
        other.save()
        user.request_friendship(other)
        self.assertEqual(Relationship.objects.all()[0].friendship, 1)
        other.request_friendship(user)
        self.assertEqual(Relationship.objects.all()[0].friendship, 3)

    def test_accept_friendship(self):
        user = ImagrUser(username=self.generator.next())
        other = ImagrUser(username=self.generator.next())
        user.save()
        other.save()
        user.request_friendship(other)
        self.assertEqual(Relationship.objects.all()[0].friendship, 1)
        other.accept_friendship(user)
        self.assertEqual(Relationship.objects.all()[0].friendship, 3)

    def test_end_friendship(self):
        user, other = self.create_friendships()
        user.end_friendship(other)
        self.assertEqual(Relationship.objects.all()[0].friendship, 0)

    def test_friends(self):
        user, other = self.create_friendships()
        self.assertEqual(user.friends()[0], other)

    def test_following(self):
        user, other = self.create_followers()
        self.assertEqual(user.following()[0], other)

    def test_followers(self):
        user, other = self.create_followers()
        self.assertEqual(other.followers()[0], user)

    def test_relationship_with(self):
        user, other = self.create_followers()
        self.assertEqual(user._relationship_with(other), Relationship.objects.all()[0])

    def _name_generator(self):
        names = [chr(n) for n in xrange(97, 123)]
        for name in names:
            yield name

    def create_friendships(self):
        user = ImagrUser(username=self.generator.next())
        other = ImagrUser(username=self.generator.next())
        user.save()
        other.save()
        user.request_friendship(other)
        self.assertEqual(Relationship.objects.all()[0].friendship, 1)
        other.accept_friendship(user)
        self.assertEqual(Relationship.objects.all()[0].friendship, 3)
        return user, other

    def create_followers(self):
        user = ImagrUser(username=self.generator.next())
        other = ImagrUser(username=self.generator.next())
        user.save()
        other.save()
        self.assertFalse(Relationship.objects.all().exists())
        user.follow(other)
        self.assertTrue(Relationship.objects.all().exists())
        return user, other
