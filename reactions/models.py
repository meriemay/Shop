from django.contrib.auth.models import Permission, User
from django.db import models
from django.conf import settings
from boutique.models import Product
from boutique.models import User
import datetime
from django.conf.urls import url
import json
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseBadRequest

import os
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.db.models import Max
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from boutique.models import Product
from posts.models import Post




class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    reaction = models.CharField(max_length=255, blank=True, null=True, 
    	choices=(('NORMAL', 'normal'), ('SMILE', 'smile'), ('LOVE', 'love'), ('WISH', 'wish'),))

    class Meta:
        unique_together = (('user', 'product'),)

    @staticmethod
    def get_choices():
        return [choice[1] for choice in Reaction._meta.get_field('reaction').choices]




class Reaction_post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    reaction = models.CharField(max_length=255, blank=True, null=True, 
        choices=(('LIKE', 'like'), ('DISLIKE', 'dislike'), ('COMMENT', 'comment')))

    class Meta:
        unique_together = (('user', 'post'),)

    @staticmethod
    def get_choices():
        return [choice[1] for choice in Reaction_post._meta.get_field('reaction').choices]


