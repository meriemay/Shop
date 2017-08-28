from django.conf.urls import url
from . import views


urlpatterns = [

url(r'^user/(?P<user_id>[0-9]+)/$', views.detail_album, name='detail_album'),
url(r'^albumm/(?P<album_id>[0-9]+)/$', views.detail_album_selected, name='detail_album_selected'),
url(r'^create_album/$', views.create_album, name='create_album'),
url(r'^pic/(?P<album_id>[0-9]+)/create_picture/$', views.create_picture, name='create_picture'),
]