from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import AlbumForm, PictureForm
from .models import Album, Picture
from project.authentication.models import Profile





def create_album(request):
    if not request.user.is_authenticated():
        return render(request, 'boutique/login.html')
    else:
        form = AlbumForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.album_logo = request.FILES['album_logo']  
            album.save()
            return render(request, 'album/detail_album.html', {'album': album})
        context = {
            "form": form,
        }
        return render(request, 'album/create_album.html', context)



def detail_album(request, user_id):
    if not request.user.is_authenticated():
        return render(request, 'boutique/login.html')
    else:
        profile = Profile.objects.get(pk = user_id)
        user = profile.user
        album =  Album.objects.filter(user=user)
        albums = Album.objects.filter(user=user)
        return render(request, 'album/detail_album.html', {'album': album, 'user': user, 'page_user': user, 'albums': album})


def detail_album_selected(request, album_id):
    if not request.user.is_authenticated():
        return render(request, 'boutique/login.html')
    else:
        user = request.user
        album = get_object_or_404(Album, pk=album_id)
        albums = Album.objects.filter(user=album.user)
        return render(request, 'album/detail_album.html', {'album': album, 'user': user, 'page_user': user,  'albums': albums})


def create_picture(request, album_id):
    form = PictureForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    albums = Album.objects.filter(user=album.user)
    user = request.user
    if form.is_valid():
        album_pictures = album.picture_set.all()
        picture = form.save(commit=False)
        picture.album = album
        picture.save()
        return render(request, 'album/detail_album.html', {'album': album,'albums': albums, 'page_user': user})
    context = {
        'album': album,
        'form': form,
        'page_user': user,
        

    }
    return render(request, 'album/create_picture.html', context)

