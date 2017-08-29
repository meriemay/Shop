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

    url(r'^product/(?P<filter_by>[a-zA_Z]+)/$', views.products, name='products'),
    url(r'^create_shop/$', views.create_shop, name='create_shop'),
    url(r'^create_wishlist/$', views.create_wishlist, name='create_wishlist'),
    url(r'^(?P<shop_id>[0-9]+)/create_product/$', views.create_product, name='create_product'),
    url(r'^(?P<shop_id>[0-9]+)/delete_product/(?P<product_id>[0-9]+)/$', views.delete_product, name='delete_product'),
    
    url(r'^(?P<shop_id>[0-9]+)/delete_shop/$', views.delete_shop, name='delete_shop'),
    url(r'^duplicate/(?P<id_product>[0-9]+)/$', views.duplicate_product, name='duplicate_product'),
    url(r'^(?P<shop_id>[0-9]+)/edit_product/(?P<product_id>[0-9]+)/$', views.edit_product, name='edit_product'),
    url(r'^(?P<shop_id>[0-9]+)/edit_product/$', views.edit_shop, name='edit_shop'),
    url(r'^(?P<shop_id>[0-9]+)/activate_product/(?P<id_product>[0-9]+)$', views.activate_product, name='activate_product'),
    url(r'^discover_product/(?P<product_id>[0-9]+)/$', views.discover_product, name='discover_product'),
    url(r'^shop/discover_shop/(?P<shop_id>[0-9]+)/$', views.discover_shop, name='discover_shop'),
    url(r'^filtrer_age/$', views.filtrer_age, name='filtrer_age'),
    

    url(r'^all_wishlists/(?P<username>[^/]+)?$', views.all_wishlists, name='all_wishlists'),
    url(r'^user_wishlists/(?P<username>[^/]+)?$', views.user_wishlists, name='user_wishlists'),
    url(r'^(?P<prod_id>[0-9]+)/add_to_wishlist/$', views.add_to_wishlist, name='add_to_wishlist'),
    url(r'^discover_wishlist/(?P<wishlist_id>[0-9]+)/$', views.discover_wishlist, name='discover_wishlist'),

]
