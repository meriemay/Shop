from django.contrib.auth.models import User
from django import forms
from .models import Post, Category_post, Comment



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['picture_attached', 'user_post', 'category']



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user_comment']