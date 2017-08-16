from __future__ import unicode_literals
import json

from django.db.models.functions import TruncMonth, TruncDay
from django.db.models import Count

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import escape
from boutique.models import Product
from posts.models import Post



class Notification(models.Model):
    NORMAL = 'normal'
    SMILE = 'smile'
    LOVE = 'love'
    WISH = 'wish'
    LIKE = 'like'
    DISLIKE = 'dislike'
    COMMENT = 'comment'

    NOTIFICATION_TYPES = (
        (NORMAL, 'normal'),
        (SMILE, 'smile'),
        (LOVE, 'love'),
        (WISH, 'wish'),
        (LIKE, 'like'),
        (DISLIKE, 'dislike'),
        (COMMENT, 'comment'),
    )


    _NORMAL_TEMPLATE = '<a href="/aa/{0}/">{1}</a> has reacted normal to your product: <a href="/boutique/discover_product/{2}/">{3}</a>'  # noqa: E501
    _SMILE_TEMPLATE = '<a href="/aa/{0}/">{1}</a> has reacted with smile to your product: <a href="/boutique/discover_product/{2}/">{3}</a>'  # noqa: E501
    _LOVE_TEMPLATE = '<a href="/aa/{0}/">{1}</a> loves your product: <a href="/boutique/discover_product/{2}/">{3}</a>'  # noqa: E501
    _WISH_TEMPLATE = '<a href="/aa/{0}/">{1}</a> wishes your product: <a href="/boutique/discover_product/{2}/">{3}</a>'  # noqa: E501
    _LIKE_TEMPLATE = '<a href="/aa/{0}/">{1}</a> likes your post: <a href="/boutique/discover_product/{2}/">{3}</a>'  # noqa: E501
    _DISLIKE_TEMPLATE = '<a href="/aa/{0}/">{1}</a> dislikes your post: <a href="/boutique/discover_product/{2}/">{3}</a>'  # noqa: E501
    _COMMENT_TEMPLATE = '<a href="/aa/{0}/">{1}</a> comments your post: <a href="/boutique/discover_product/{2}/">{3}</a>'  # noqa: E501

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=255, choices=NOTIFICATION_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ('-date',)

    def __str__(self):
        if self.type == self.NORMAL:
            return self._NORMAL_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.product.pk,
                escape(self.get_summary(self.product.product_name))
                )
        elif self.type == self.SMILE:
            return self._SMILE_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.product.pk,
                escape(self.get_summary(self.product.product_name))
                )
        elif self.type == self.LOVE:
            return self._LOVE_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.product.pk,
                escape(self.get_summary(self.product.product_name))
                )
        elif self.type == self.WISH:
            return self._WISH_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.product.pk,
                escape(self.get_summary(self.product.product_name))
                )
        elif self.type == self.LIKE:
            return self._LIKE_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.post.pk,
                escape(self.get_summary(self.post.user_post))
                )
        elif self.type == self.DISLIKE:
            return self._DISLIKE_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.post.pk,
                escape(self.get_summary(self.post.user_post))
                )
        elif self.type == self.COMMENT:
            return self._COMMENT_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.post.pk,
                escape(self.get_summary(self.post.user_post))
                )
        
        else:
            return 'Ooops! Something went wrong.'

    def get_summary(self, value):
        summary_size = 50
        if len(value) > summary_size:
            return '{0}...'.format(value[:summary_size])

        else:
            return value
    

    def send(from_user, to_user, product, type):
        notification = Notification(from_user=from_user,
                                    to_user=to_user,
                                    product=product,
                                   
                                    type=type).save()
        return notification

    def send_post(from_user, to_user, post, type):
        notification = Notification(from_user=from_user,
                                    to_user=to_user,
                                    
                                    post=post,
                                    type=type).save()
        return notification

