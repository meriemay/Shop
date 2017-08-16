from __future__ import unicode_literals
import os

from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from boutique.models import Product
from django.db.models import Max
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Message(models.Model):
    user = models.ForeignKey(User, related_name='+')
    message = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(User, related_name='+')
    from_user = models.ForeignKey(User, related_name='+')
    is_read = models.BooleanField(default=False)
    product = models.ForeignKey(Product, null=True)
    

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
        ordering = ('date',)
        db_table = 'messages_message'

    
    @staticmethod
    def send_message(from_user, to_user, message, product):
        
        current_user_message = Message(from_user=from_user,
                                       message=message,
                                       user=from_user,
                                       product=product,
                                    

                                       conversation=to_user,
                                       is_read=True)
        current_user_message.save()
        Message(from_user=from_user,
                conversation=from_user,
                message=message,
                product=product,
               
                user=to_user).save()

        return current_user_message

    @staticmethod
    def get_conversations(user):
        conversations = Message.objects.filter(
            user=user).values('conversation').annotate(
                last=Max('date')).order_by('-last')
        users = []
        for conversation in conversations:
            users.append({
                'user': User.objects.get(pk=conversation['conversation']),
                'last': conversation['last'],
                'unread': Message.objects.filter(user=user,
                                                 conversation__pk=conversation[
                                                    'conversation'],
                                                 is_read=False).count(),
                })

        return users



class Picture(models.Model): 
    message = models.OneToOneField(Message, on_delete = models.CASCADE)   
    image = models.ImageField(null=True, blank=True)   

