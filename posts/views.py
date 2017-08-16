from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
import re
from django.shortcuts import redirect, render
from .forms import PostForm, CommentForm
from .models import Post, Comment, Category_post
from boutique.models import Product




def create_post(request): 
	user =request.user
	if request.method == 'POST':
		form = PostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return render(request, 'posts/discover_post.html', {'post': post})
	form = PostForm()
	posts = Post.objects.filter(user=user)
	return render(request, 'posts/create_post.html', {'form':form , 'posts' : posts})




def commenter(request, post_id): 
    user =request.user
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user= user
            comment.user_post = post
            comment.save()
            return render(request, 'posts/one_comment.html', {'comment': comment})
    form = CommentForm()
    comments = Comment.objects.filter(user=user)
    return render(request, 'posts/commentaire.html', {'form':form , 'comments' : comments, 'post': post})




def hi(request):
    products = Product.objects.filter(is_activate=True)[:4]
    posts = Post.objects.all()[:4]

    return render(request, 'posts/home.html', {'products': products, 'posts':posts})



def filtrer_posts(request, category=''):
    posts = Post.objects.all()
    
    categories = Category_post.objects.all()

    counter = []
    header1 = ''
    
    
    for cat in categories:
        counter.append((cat, posts.filter(category=cat).count()))

    if not category == '':
        posts = posts.filter(category__label=category)

    if 'search' in request.GET:
        query = request.GET.get('search')
        query_list = re.sub("[^\w]", " ", query).split()
        q = Q()
        for word in query_list:
            q |= Q(user_post__icontains=word) 
        posts = posts.filter(q)
        header1 = 'Search = ' + query



    counter = []
    for c in categories:
        counter.append((c, posts.filter(category=c).count()))


    page = request.GET.get('page')
    paginator = Paginator(posts, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'header1': header1,
       
        'counter': counter,
        'posts': posts,
        'categories': categories,
        'page': page
    }

    return render(request, 'posts/discover_all_posts.html',{'posts': posts, 'page':page, 'categories': categories, 'counter': counter})
