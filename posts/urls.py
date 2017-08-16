from django.conf.urls import url
from . import views
urlpatterns = [
	
	url(r'^create_post/$', views.create_post, name='create_post'),
	url(r'^filtrer_posts/$', views.filtrer_posts, name='filtrer_posts'),
	url(r'^commenter/(?P<post_id>[0-9]+)$', views.commenter, name='commenter'),

	
    url(r'^discover/(?P<category>[\w\-]+)/$', views.filtrer_posts, name='filtrer_posts'),
    
    url(r'^$', views.hi, name='hi'),
    

]