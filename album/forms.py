from django.contrib.auth.models import User
from django import forms
from .models import Album, Picture


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['album_name', 'album_logo', 'album_description']


class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ['picture_description', 'pic']