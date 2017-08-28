from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Max, Min
import re
from project.authentication.models import Profile
from django.shortcuts import redirect
from .forms import ShopForm, ProductForm, UserForm, CommercantForm, WishListForm
from .models import Shop, Product, Category, User, Commercant, Wishlist





def create_shop(request):
    if not request.user.is_authenticated():
        return render(request, 'boutique/login.html')
    elif not hasattr(request.user, 'commercant'):
        form = CommercantForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            commercant = form.save(commit=False)
            commercant.user = request.user
            commercant.save()
            return render(request, 'boutique/create_shop.html/')
        context = {
            "form_name": "You have to be a Store Keeper",
            "form": form,
        }
        return render(request, 'boutique/form_template_commercant.html', context)
    
    else:
        form = ShopForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.user = request.user
            shop.shop_logo = request.FILES['shop_logo']
            file_type = shop.shop_logo.url.split('.')[-1]
            file_type = file_type.lower()
            # if file_type not in IMAGE_FILE_TYPES:
            #     context = {
            #         'shop': shop,
            #         'form': form,
            #         'error_message': 'Image file must be PNG, JPG, or JPEG',
            #     }
                # return render(request, 'boutique/create_shop.html', context)
            shop.save()
            return render(request, 'boutique/detail.html', {'shop': shop})
        context = {
            "form": form,
        }
        return render(request, 'boutique/create_shop.html', context)



def create_product(request, shop_id):
    form = ProductForm(request.POST or None, request.FILES or None)
    shop = get_object_or_404(Shop, pk=shop_id)
    if form.is_valid():
        shops_products = shop.product_set.all()
        for s in shops_products:
            if s.product_name == form.cleaned_data.get("product_name"):
                context = {
                    'shop': shop,
                    'form': form,
                    'error_message': 'You already added that product',
                }
                return render(request, 'boutique/create_product.html', context)
        product = form.save(commit=False)
        product.shop = shop


        product.save()
        return render(request, 'boutique/detail.html', {'shop': shop})
    context = {
        'shop': shop,
        'form': form,
    }
    return render(request, 'boutique/create_product.html', context)


def delete_shop(request, shop_id):
    shop = Shop.objects.get(pk=shop_id)
    shop.delete()
    shops = Shop.objects.filter(user=request.user)
    return render(request, 'boutique/index.html', {'shops': shops})


def delete_product(request, shop_id, product_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    product = Product.objects.get(pk=product_id)
    product.delete()
    return render(request, 'boutique/detail.html', {'shop': shop})


def detail(request, shop_id):
    if not request.user.is_authenticated():
        return render(request, 'boutique/login.html')
    else:
        user = request.user
        shop = get_object_or_404(Shop, pk=shop_id)
        return render(request, 'boutique/detail.html', {'shop': shop, 'user': user})

def discover_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'boutique/discover_product.html', {'product': product})






def favorite(request, product_id):
    if not request.user.is_authenticated():
        return render(request, 'boutique/login.html')
    else:
        product = get_object_or_404(Product, pk=product_id)
        try:
            if product.is_favorite:
                Product.is_favorite = False
            else:
                Product.is_favorite = True
            product.save()
        except (KeyError, Product.DoesNotExist):
            return JsonResponse({'success': False})
        else:
            return JsonResponse({'success': True})


def create_wishlist(request):
    user =request.user
    wishlists = Wishlist.objects.filter(user=user)
    if not request.user.is_authenticated():
        return render(request, 'boutique/login.html')
    else:
        form = WishListForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            wishlist = form.save(commit=False)
            wishlist.user = request.user
           
            wishlist.save()
            return render(request, 'boutique/discover_wishlists.html', {'wishlist': wishlist, 'wishlists': wishlists})
          
        context = {
            "form": form,
            
        }
         

        return render(request, 'boutique/create_wishlist.html', context, {'wishlists': wishlists})



def user_wishlists(request, username):
    
    wishlists = Wishlist.objects.all()

    print(wishlists)
    return render(request, 'boutique/discover_wishlists.html',{'wishlists': wishlists, 'username': username})


def add_to_wishlist(request, prod_id):
    user=request.user
    prod = get_object_or_404(Product, pk=prod_id)
    wishlists = Wishlist.objects.filter(user=user)

    for w in wishlists:
        name = request.POST.get(w.name)
        print(prod.name)
        print(w.name)
        print(name)
        if name:
            w.product.add(prod)
            w.save()
    return HttpResponseRedirect(reverse_lazy('boutique:filtrer'))





# def favorite_shop(request, shop_id):
#     shop = get_object_or_404(Shop, pk=shop_id)
#     try:
#         if shop.is_favorite:
#             shop.is_favorite = False
#         else:
#             shop.is_favorite = True
#         shop.save()
#     except (KeyError, Shop.DoesNotExist):
#         return JsonResponse({'success': False})
#     else:
#         return JsonResponse({'success': True})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'boutique/login.html')
    else:
        shops = Shop.objects.filter(user=request.user)
        product_results = Product.objects.all()
        query = request.GET.get("q")
        if query:
            shops = shops.filter(
                Q(shop_name__icontains=query)
            ).distinct()
            product_results = product_results.filter(
                Q(product_name__icontains=query)
            ).distinct()
            return render(request, 'boutique/search.html', {
                'shops': shops,
                'products': product_results,
            })
        else:
            return render(request, 'boutique/index.html', {'shops': shops})
 
 
def shops(request):
    if not request.user.is_authenticated():
        return render(request, 'boutique/login.html')
    else:
        shops = Shop.objects.all()
        product_results = Product.objects.all()
        return render(request, 'boutique/discover_shop.html', {'shops': shops})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'boutique/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password_login = request.POST['password_login']
        user = authenticate(username=username, password=password_login)
        if user is not None:
            if user.is_active:
                login(request, user)
                shops = Shop.objects.filter(user=request.user)
                return render(request, 'boutique/index.html', {'shops': shops})
            else:
                return render(request, 'boutique/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'boutique/login.html', {'error_message': 'Invalid login'})
    return render(request, 'boutique/login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            user = User.objects.create_user(username=username,
                                            email=username,
                                            password=password1)
            if user is not None:
                if user.is_active:
                    user = authenticate(username=username, password=password1)
                    login(request, user)
                    products = Product.objects.all()
                    return render(request, 'boutique/discover.html', {'products': products})
    return render(request, 'boutique/login.html')


def products(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'boutique/login.html')
    else:
        try:
            product_ids = []
            for shop in Shop.objects.filter(user=request.user):
                for product in shop.product_set.all():
                    product_ids.append(product.pk)
            users_products = Product.objects.filter(pk__in=product_ids)
            if filter_by == 'favorites':
                users_products = users_products.filter(is_favorite=True)
        except Shop.DoesNotExist:
            users_products = []
        return render(request, 'boutique/products.html', {
            'product_list': users_products,
            'filter_by': filter_by,
        })



def duplicate_product(request, id_product):
    product = Product.objects.get(id=id_product)
    product.id = None
    product.save()
    return redirect('/boutique/' + str(product.shop.id))


def edit_product(request, shop_id, product_id):
    boutique = get_object_or_404(Shop, pk=shop_id)
    instance = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        return HttpResponseRedirect('/boutique/' + str(instance.shop.id))
    context = {
        'shop': boutique,
        'form': form,
    }
    return render(request,'boutique/product_form.html', context)

def edit_shop(request, shop_id):
    boutique = get_object_or_404(Shop, pk=shop_id)
    form = ShopForm(request.POST or None, request.FILES or None, instance=boutique)
    if form.is_valid():
        boutique = form.save(commit = False)
        boutique.save()
        return HttpResponseRedirect('/boutique/' )
    context = {
        'shop': boutique,
        'form': form,
    }
    return render(request,'boutique/create_shop.html', context)

def activate_product(request,shop_id, id_product):
    product = Product.objects.get(id=id_product)
    boutique_id = product.shop.id
    shop = Shop.objects.get(id = boutique_id)
    if product.is_activate == True:
           
        product.is_activate = False
    else:
         
        product.is_activate = True
    product.save()
    return render(request, 'boutique/detail.html', {'shop': shop})



# def discover(request):
#     products = Product.objects.all()
#     page = request.GET.get('page')
#     paginator = Paginator(products, 3)
#     try:
#         products = paginator.page(page)
#     except PageNotAnInteger:
#         products = paginator.page(1)
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)
#     return render(request, 'boutique/discover.html', {'products': products, 'page': page})
def filtrer_age(request, category=''):
    counter = []
    header1 = ''
    header2 = ''
    header3 = ''
    header4 = ''
    header5 = ''

    categories = Category.objects.all()
    age = int(request.user.profile.age)
    if age<3 :
        type_age='baby'
    elif age>3 and age<12:
        type_age='child'
    elif age>12 and age<21:
        type_age='teenager'
    else:
        type_age='adult'
    products1 = Product.objects.filter(age=type_age)
    products2 = Product.objects.all().exclude(age=type_age)

    
    var = request.GET.get("slider",'0,5000')
    value = var.split(',')
    min_slider = int(value[0]) 
    max_slider = int(value[1])
    print(max_slider)

    products = Product.objects.filter(Q(product_price__lte=max_slider)& Q(product_price__gte=min_slider)).distinct()
    
    for cat in categories:
        counter.append((cat, products.filter(category=cat).count()))

    if not category == '':
        products = products.filter(category__label=category)

    if 'search' in request.GET:
        query = request.GET.get('search')
        query_list = re.sub("[^\w]", " ", query).split()
        q = Q()
        for word in query_list:
            q |= Q(product_name__icontains=word) | Q(description__icontains=word) | Q(tags__icontains=word)
        products = products.filter(q)
        header1 = 'Search = ' + query



    max_price = products.aggregate(Max('product_price'))
    min_price = products.aggregate(Min('product_price'))

    
    if ('product_type' in request.GET):
        product_type =request.GET.get('product_type')

        q = Q(product_type = product_type)
        products = products.filter(q)
        if product_type == 'Vintage':
            product_type_label = 'Vintage'
        elif product_type == 'Hand_Made':
            product_type_label = 'Hand_Made'
        print(Product.Vintage)
        header3= 'Product type = '+ str(product_type_label)



    if ('gender' in request.GET):
        gender =request.GET.get('gender')

        q = Q(gender = gender)
        products = products.filter(q)
        if gender == 'Male':
            gender_label = 'Male'
        elif gender == 'Female':
            gender_label = 'Female'
        print(Product.Male)
        header4= 'gender = '+ str(gender_label)



    if ('age' in request.GET):
        age =request.GET.get('age')

        q = Q(age = age)
        products = products.filter(q)
        if age == 'Baby':
            age_label = 'Baby'
        elif age == 'Child':
            age_label = 'Child'
        elif age == 'Teenager':
            age_label = 'Teenager'
        elif age == 'Adult':
            age_label = 'Adult'
        header5= 'age = '+ str(age_label)


    if ('ordering' in request.GET):
        ordering = request.GET.get('ordering')
        if ordering == 'recent':
            products = products.order_by('create_date')
        elif ordering == 'price_asc':
            products = products.order_by('product_price')
        elif ordering == 'price_desc':
            products = products.order_by('-product_price')
        header2= 'Ordered by '+ str(ordering)
    else:
        products.order_by('create_date')
        header2= 'Ordered by recent'



    
    counter = []
    for c in categories:
        counter.append((c, products.filter(category=c).count()))

    page = request.GET.get('page')
    paginator = Paginator(products, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'header1': header1,
        'header2': header2,
        'header3': header3,
        'header4': header4,
        'header5': header5,
        'counter': counter,
        'products': products,
        'categories': categories,
        'page': page
    }


    return render(request, 'boutique/discover.html', {'products1': products1, 'products2': products2, 'counter': counter,
        'products': products,
        'categories': categories,
        'page': page})



def discover_shop(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    products = Product.objects.filter(shop=shop)

    if 'search' in request.GET:
        query = request.GET.get('search')
        query_list = re.sub("[^\w]", " ", query).split()
        q = Q()
        for word in query_list:
            q |= Q(product_name__icontains=word) | Q(description__icontains=word) | Q(tags__icontains=word)
        products = products.filter(q)
        header1 = 'Search = ' + query

   
    


    return render(request, 'boutique/discover_shop.html', {'products': products, 'shop':shop})



def filtrer(request, category=''):

    products = Product.objects.filter(is_activate=True)
    all_products = Product.objects.filter(is_activate=True)
    categories = Category.objects.all()
    counter = []
    header1 = ''
    header2 = ''
    header3 = ''
    header4 = ''
    header5 = ''
    var = request.GET.get("slider",'0,5000')
    value = var.split(',')
    min_slider = int(value[0]) 
    max_slider = int(value[1])
    print(max_slider)

    products = Product.objects.filter(Q(product_price__lte=max_slider)& Q(product_price__gte=min_slider)).distinct()
    
    for cat in categories:
        counter.append((cat, products.filter(category=cat).count()))

    if not category == '':
        products = products.filter(category__label=category)

    if 'search' in request.GET:
        query = request.GET.get('search')
        query_list = re.sub("[^\w]", " ", query).split()
        q = Q()
        for word in query_list:
            q |= Q(product_name__icontains=word) | Q(description__icontains=word) | Q(tags__icontains=word)
        products = products.filter(q)
        header1 = 'Search = ' + query



    max_price = products.aggregate(Max('product_price'))
    min_price = products.aggregate(Min('product_price'))

    
    if ('product_type' in request.GET):
        product_type =request.GET.get('product_type')

        q = Q(product_type = product_type)
        products = products.filter(q)
        if product_type == 'Vintage':
            product_type_label = 'Vintage'
        elif product_type == 'Hand_Made':
            product_type_label = 'Hand_Made'
        print(Product.Vintage)
        header3= 'Product type = '+ str(product_type_label)



    if ('gender' in request.GET):
        gender =request.GET.get('gender')

        q = Q(gender = gender)
        products = products.filter(q)
        if gender == 'Male':
            gender_label = 'Male'
        elif gender == 'Female':
            gender_label = 'Female'
        print(Product.Male)
        header4= 'gender = '+ str(gender_label)



    if ('age' in request.GET):
        age =request.GET.get('age')

        q = Q(age = age)
        products = products.filter(q)
        if age == 'Baby':
            age_label = 'Baby'
        elif age == 'Child':
            age_label = 'Child'
        elif age == 'Teenager':
            age_label = 'Teenager'
        elif age == 'Adult':
            age_label = 'Adult'
        header5= 'age = '+ str(age_label)


    if ('ordering' in request.GET):
        ordering = request.GET.get('ordering')
        if ordering == 'recent':
            products = products.order_by('create_date')
        elif ordering == 'price_asc':
            products = products.order_by('product_price')
        elif ordering == 'price_desc':
            products = products.order_by('-product_price')
        header2= 'Ordered by '+ str(ordering)
    else:
        products.order_by('create_date')
        header2= 'Ordered by recent'



    
    counter = []
    for c in categories:
        counter.append((c, products.filter(category=c).count()))

    page = request.GET.get('page')
    paginator = Paginator(products, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'header1': header1,
        'header2': header2,
        'header3': header3,
        'header4': header4,
        'header5': header5,
        'counter': counter,
        'products': products,
        'categories': categories,
        'page': page
    }

    return render(request, 'boutique/discover.html', {'counter': counter,
        'products': products,
        'categories': categories,
        'page': page})



