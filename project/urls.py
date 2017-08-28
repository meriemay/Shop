from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from project.authentication import views as project_auth_views
from project.core import views as core_views
from project.authentication import views as bootcamp_auth_views
from django.contrib.auth import views as auth_views
from reactions import views as reactions_views
from notifications import views as notifications_views
from posts import views as posts_views

urlpatterns = [
    
    url(r'^reaction/(?P<pk>\d+)$', reactions_views.react, name='react'),
    url(r'^reaction_post/(?P<pk>\d+)$', reactions_views.react_post, name='react_post'),
    url(r'^admin/', admin.site.urls),
    url(r'^boutique/', include('boutique.urls')),
    url(r'^post/', include('posts.urls')),
    url(r'^album/', include('album.urls')),

    url(r'^', include('boutique.urls')),
   	url(r'^messages/', include('project.messenger.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^network/$', core_views.network, name='network'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^feeds/', include('project.feeds.urls')),
    url(r'^$', core_views.home, name='home'),
    url(r'^login', auth_views.login, {'template_name': 'core/cover.html'},
        name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', bootcamp_auth_views.signup, name='signup'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/picture/$', core_views.picture, name='picture'),
    url(r'^settings/upload_picture/$', core_views.upload_picture,
        name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', core_views.save_uploaded_picture,
        name='save_uploaded_picture'),
    url(r'^aa/(?P<username>[^/]+)/$', core_views.profile, name='profile'),
     url(r'^notifications/$', notifications_views.notifications,
        name='notifications'),
    url(r'^notifications/last/$', notifications_views.last_notifications,
        name='last_notifications'),
    url(r'^notifications/check/$', notifications_views.check_notifications,
        name='check_notifications'),
    
    url(r'^api/notifications/', include("notifications.api.urls", namespace='notifications-api')),
    url(r'^api/messenger/', include("project.messenger.api.urls", namespace='messenger-api')),
    url(r'^api/reactions/', include("reactions.api.urls", namespace='reactions-api')),
    

]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
