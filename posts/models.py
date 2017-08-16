from django.contrib.auth.models import Permission, User
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _

import bleach


def user_directory_path(instance, filename):
    return 'post_{0}/{1}'.format(instance.user, str(timezone.now)+str(filename))

def category_directory_path(instance, filename):
    return 'category_{0}'.format(str(timezone.now)+str(filename))

class Category_post(models.Model):
	picture = models.ImageField(blank=True, null=True, upload_to=category_directory_path)
	label = models.CharField(
        max_length=250, 
        null=True 
    )



	def __str__(self):
		return self.picture.url



class Post(models.Model):
	user = models.ForeignKey(User, default=1)
	picture_attached = models.ImageField(blank=True, null=True, upload_to=user_directory_path)
	user_post = models.TextField(max_length=255, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category_post, on_delete=models.CASCADE, null=True,
        blank=True)

	def __str__(self):
		return self.user_post

	class Meta:
		ordering = ('-date',)






class Comment(models.Model):
	user = models.ForeignKey(User)
	user_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments')
	date = models.DateTimeField(auto_now_add=True)
	user_comment = models.TextField(max_length=255)

	def __str__(self):
		return self.user_comment
	
