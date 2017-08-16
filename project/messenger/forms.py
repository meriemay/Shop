from django.contrib.auth.models import User
from django import forms
from project.messenger.models import Picture


class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ['image']