from django.conf.urls import url
from django.contrib import admin

from .views import (
    InteractAPIView,)

urlpatterns = [
    url(r'^react/(?P<prod_id>[0-9]+)/$',InteractAPIView.as_view(), name='react'),
]