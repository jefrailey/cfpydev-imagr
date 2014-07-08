from django.shortcuts import render
from django.http import HttpResponse as Response


# Create your views here.
def front_page():
    u"""shows anonymous users something nice to encourage them to sign up"""
    pass


def home_page():
    u"""shows logged-in users a list of their albums, with a representative
    image from each album
    """
    pass


def album_page():
    u"""shows logged-in users a display of photos in a single album"""
    pass


def photo_page():
    u"""shows logged-in users a single photo along with details about it."""
    pass


def stream_page():
    u"""shows users their most recent photos along with recent photos uploaded
    by friends or those they are following.
    """
    pass
