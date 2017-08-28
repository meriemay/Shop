from django.contrib import admin
from .models import Shop, Product, Category, Wishlist
from project.messenger.models import Message, Picture
from reactions.models import Reaction
from posts.models import Category_post
from posts.models import Post, Comment
from album.models import Album

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(Picture)
admin.site.register(Reaction)
admin.site.register(Category_post)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Album)
admin.site.register(Wishlist)


