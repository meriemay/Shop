from django.conf.urls import url
from django.contrib import admin

from . views import (
        NotificationListAPIView,
)

urlpatterns = [
    url(r'^(?P<username>[-\w]+)/$',NotificationListAPIView.as_view(), name='notification_list')
]