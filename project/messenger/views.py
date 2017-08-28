import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render

from project.decorators import ajax_required
from project.messenger.models import Message
from project.messenger.forms import PictureForm
from boutique.models import Product, Picture, Commercant
from django.db.models import Q



@login_required
def inbox(request):    
    conversations = Message.get_conversations(user=request.user)
    active_conversation = None
    messages = None
    products = None
    if conversations:
        conversation = conversations[0]
        active_conversation = conversation['user'].username
        messages = Message.objects.filter(user=request.user,
                                          conversation=conversation['user'])
        messages.update(is_read=True)
        for conversation in conversations:
            if conversation['user'].username == active_conversation:
                conversation['unread'] = 0
        products = Product.objects.filter(Q(shop__user__username=request.user) | Q(shop__user__username=active_conversation))
        if not products:
            products=Product.objects.all()   
    return render(request, 'messenger/inbox.html', {
        'messages': messages,
        'conversations': conversations,
        'active': active_conversation,
        'products':products
        })


@login_required
def messages(request, username):
    conversations = Message.get_conversations(user=request.user)
    active_conversation = username
    messages = Message.objects.filter(user=request.user,
                                      conversation__username=username)
    messages.update(is_read=True)
    for conversation in conversations:
        if conversation['user'].username == username:
            conversation['unread'] = 0
        products = Product.objects.filter(Q(shop__user__username=request.user) | Q(shop__user__username=username))
        if not products:
            products=Product.objects.all()
    return render(request, 'messenger/inbox.html', {
        'messages': messages,
        'conversations': conversations,
        'active': active_conversation,
        'products':products
        })


@login_required
def new(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        from_user = request.user
        to_user_username = request.POST.get('to')
        try:
            to_user = User.objects.get(username=to_user_username)

        except Exception:
            try:
                to_user_username = to_user_username[
                    to_user_username.rfind('(')+1:len(to_user_username)-1]
                to_user = User.objects.get(username=to_user_username)

            except Exception:
                return redirect('/messages/new/')

        message = request.POST.get('message')
        if len(message.strip()) == 0:
            return redirect('/messages/new/')

        if from_user != to_user:
            Message.send_message(from_user, to_user, message, product=None)

        return redirect('/messages/{0}/'.format(to_user_username))

    else:
        conversations = Message.get_conversations(user=request.user)
        return render(request, 'messenger/new.html',
                      {'conversations': conversations})


@login_required
def new2(request, prod_id):
    form = PictureForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        from_user = request.user
        prod=Product.objects.get(id=prod_id)

        touser=User.objects.get(shop__product=prod)
        to_user_username=touser.username
        # to_user_username = request.POST.get('to')
        
        try:
            to_user = User.objects.get(username=to_user_username)

        except Exception:
            try:
                to_user_username = to_user_username[
                    to_user_username.rfind('(')+1:len(to_user_username)-1]
                to_user = User.objects.get(username=to_user_username)

            except Exception:
                return redirect('/messages/')

        message = request.POST.get('message')
        if len(message.strip()) == 0:
            return redirect('/messages/')

        if from_user != to_user:
            
            x = form.save(commit=False)
            msg = Message.send_message(from_user, to_user, message, product=None)
            x.message = msg
            x.save()

        return redirect('/messages/{0}/'.format(to_user_username))

    else:
        conversations = Message.get_conversations(user=request.user)
        return render(request, 'messenger/new2.html',
                      {'conversations': conversations, 'prod_id': prod_id})


@login_required
@ajax_required
def delete(request):
    return HttpResponse()


@login_required

def send(request):
    if request.method == 'POST':
        from_user = request.user
        to_user_username = request.POST.get('to')
        to_user = User.objects.get(username=to_user_username)
        message = request.POST.get('message')
        form = PictureForm(request.POST, request.FILES)
        
        if from_user != to_user:
            x = form.save(commit=False)
            msg = Message.send_message(from_user, to_user, message, product=None)
            x.message = msg
            x.save()
            # return render(request, 'messenger/includes/partial_message.html',
            #               {'message': msg})
            return redirect('/messages/{0}/'.format(to_user_username))
            
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


@login_required
@ajax_required
def users(request):
    users = User.objects.filter(is_active=True)
    dump = []
    template = '{0} ({1})'
    for user in users:
        if user.profile.get_screen_name() != user.username:
            dump.append(template.format(user.profile.get_screen_name(),
                                        user.username))
        else:
            dump.append(user.username)
    data = json.dumps(dump)
    return HttpResponse(data, content_type='application/json')


@login_required
@ajax_required
def check(request):
    count = Message.objects.filter(user=request.user, is_read=False).count()
    return HttpResponse(count)



def attach(request):
    conversations = Message.get_conversations(user=request.user)
    active_conversation = username
    messages = Message.objects.filter(user=request.user,
                                      conversation__username=username)
    messages.update(is_read=True)
    for conversation in conversations:
        if conversation['user'].username == username:
            conversation['unread'] = 0
        products = Product.objects.filter(Q(shop__user__username=request.user) | Q(shop__user__username=username))
        if not products:
            products=Product.objects.all()
        to_user = request.POST.get('to_user')
    

    # Pagination
    page = request.GET.get('page')
    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'messenger/inbox.html', {'products': products, 'page': page, 'to_user':to_user})


def send_product(request):
    if request.method == 'POST':
        from_user = request.user
        to_user_username = request.POST.get('to_user')
        to_user = User.objects.get(username=to_user_username)
        print(to_user)
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        form = PictureForm(request.POST, request.FILES)
        name = product.product_name
        
        if from_user != to_user:
            x = form.save(commit=False)
            msg = Message.send_message(from_user, to_user,message=name, product=product)
            x.message = msg
            x.save()
            # return render(request, 'messenger/includes/partial_message.html',
            #               {'message': msg})
            return redirect('/messages/{0}/'.format(to_user_username))
            
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

def search_modal(request):
    products = Product.objects.filter(shop__user__username=request.user)
    recherch= request.GET.get('search')
    if recherch:
        produits= products.filter(Q(product_name__icontains=recherch)).distinct()

    return render(request, 'messenger/result_search_modal.html',{
               
                'products': produits
                })

    