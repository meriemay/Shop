import json
from boutique.models import Product, Shop
import os
from django.db import models
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from reactions.models import Reaction, Reaction_post
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import generic
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from notifications.models import Notification
from posts.models import Post




def react(request, pk):

    data = {}
    product = Product.objects.get(pk=pk)
    reaction = request.GET.get('reaction')
    has_reacted = Reaction.objects.filter(user=request.user, product=product).count() == 1
    reaction_choices = Reaction.get_choices()
    obj=product.reaction_set.filter(reaction="smile").count()
    if has_reacted:
        reaction_obj = request.user.reaction_set.get(product=product)
        if reaction in reaction_choices:

            if reaction_obj.reaction != reaction:
                reaction_obj.reaction = reaction
                Notification.send(from_user=request.user, to_user=product.shop.user, product=product, type=reaction)
                reaction_obj.save()
        		
            else:
                reaction_obj.delete()
            data['reaction'] = reaction

        elif not reaction:
            reaction_obj.delete()
            data['reaction'] = ''

    elif reaction in reaction_choices:
        Reaction.objects.create(user=request.user, product=product, reaction=reaction)
        Notification.send(from_user=request.user, to_user=product.shop.user, product=product, type=reaction)

        data['reaction'] = reaction;
       
        
    data['count'] = product.reaction_set.count()
    print(reaction)
    #data['count_smile']= obj
    normal= Reaction.objects.filter(product= product, reaction='normal').count()
    smile= Reaction.objects.filter(product= product, reaction='smile').count()
    love= Reaction.objects.filter(product= product, reaction='love').count() 
    wish= Reaction.objects.filter(product= product, reaction='wish').count()
    data['normal'] = normal
    data['smile'] = smile
    data['love'] = love
    data['wish'] = wish
    print(data)
   

    
    return HttpResponse(json.dumps(data), content_type='application/json')





def react_post(request, pk):

    data = {}
    post = Post.objects.get(pk=pk)
    reaction = request.GET.get('reaction')
    has_reacted = Reaction_post.objects.filter(user=request.user, post=post).count() == 1
    reaction_choices = Reaction_post.get_choices()
   
    if has_reacted:
        reaction_obj = request.user.reaction_post_set.get(post=post)
        if reaction in reaction_choices:

            if reaction_obj.reaction != reaction:
                reaction_obj.reaction = reaction
                Notification.send_post(from_user=request.user, to_user=post.user, post=post, type=reaction)
                reaction_obj.save()
                
            else:
                reaction_obj.delete()
            data['reaction'] = reaction

        elif not reaction:
            reaction_obj.delete()
            data['reaction'] = ''

    elif reaction in reaction_choices:
        Reaction_post.objects.create(user=request.user, post=post, reaction=reaction)
        Notification.send_post(from_user=request.user, to_user=post.user, post=post, type=reaction)

        data['reaction'] = reaction;
       
        
    data['count'] = post.reaction_post_set.count()

    print(reaction)
   

    like= Reaction_post.objects.filter(post= post, reaction='like').count()
    dislike= Reaction_post.objects.filter(post= post, reaction='dislike').count()
    comment= Reaction_post.objects.filter(post= post, reaction='comment').count()
   
    data['like'] = like
    data['dislike'] = dislike
    data['comment'] = comment
    
    print(data)
   

    
    return HttpResponse(json.dumps(data), content_type='application/json')


