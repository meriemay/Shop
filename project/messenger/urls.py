from django.conf.urls import url
from project.messenger import views

urlpatterns = [

	url(r'^attach/$', views.attach, name='attach_product'),
    url(r'^search_modal/$', views.search_modal, name='search_modal'),
    url(r'^$', views.inbox, name='inbox'),
    url(r'^new/$', views.new, name='new_message'),
    url(r'^new2/(?P<prod_id>[^/]+)/$', views.new2, name='new_message2'),
    url(r'^send/$', views.send, name='send_message'),
    url(r'^send_prod/$', views.send_product, name='send_product'),
    url(r'^delete/$', views.delete, name='delete_message'),
    url(r'^users/$', views.users, name='users_message'),
    url(r'^check/$', views.check, name='check_message'),
    url(r'^(?P<username>[^/]+)/$', views.messages, name='messages'),


     
]
