from django.conf.urls import url
from django.contrib import admin

from .views import (
    MessageListAPIView,
    MessageSendAPIView)

urlpatterns = [
    url(r'^get/(?P<username>[-\w]+)/$',MessageListAPIView.as_view(), name='message_list'),
    url(r'^send/(?P<to_user>[-\w]+)/$',MessageSendAPIView.as_view(), name='send_message'),
]