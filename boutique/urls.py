

from django.conf.urls import url
from . import views

app_name = 'boutique'

urlpatterns = [
    url(r'^filtrer/$', views.filtrer, name='filtrer'),
    url(r'^discover/(?P<category>[\w\-]+)/$', views.filtrer, name='filtrer'),
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<shop_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<product_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^product/(?P<filter_by>[a-zA_Z]+)/$', views.products, name='products'),
    url(r'^create_shop/$', views.create_shop, name='create_shop'),
    url(r'^(?P<shop_id>[0-9]+)/create_product/$', views.create_product, name='create_product'),
    url(r'^(?P<shop_id>[0-9]+)/delete_product/(?P<product_id>[0-9]+)/$', views.delete_product, name='delete_product'),
    url(r'^(?P<shop_id>[0-9]+)/favorite_shop/$', views.favorite_shop, name='favorite_shop'),
    url(r'^(?P<shop_id>[0-9]+)/delete_shop/$', views.delete_shop, name='delete_shop'),
    url(r'^duplicate/(?P<id_product>[0-9]+)/$', views.duplicate_product, name='duplicate_product'),
    url(r'^(?P<shop_id>[0-9]+)/edit_product/(?P<product_id>[0-9]+)/$', views.edit_product, name='edit_product'),
    url(r'^(?P<shop_id>[0-9]+)/edit_product/$', views.edit_shop, name='edit_shop'),
    url(r'^(?P<shop_id>[0-9]+)/activate_product/(?P<id_product>[0-9]+)$', views.activate_product, name='activate_product'),
    url(r'^discover_product/(?P<product_id>[0-9]+)/$', views.discover_product, name='discover_product'),
    
]
