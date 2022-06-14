from django.shortcuts import render
from .models import Page, Post, Song
# Create your views here.
from django.contrib.auth.models import User


def home(request):
    return render(request, 'myapp/home.html')


def user(request):
    users1 = User.objects.filter(mypage__pageCat='War')
    users2 = User.objects.filter(post__post_title='Ukrain War')
    users3 = User.objects.filter(song__song_duration=20)
    context = {
        'users1': users1,
        'users2': users2,
        'users3': users3,
    }
    return render(request, 'myapp/user.html', context)


def page(request):
    page = Page.objects.filter(user__username='moni')

    context = {
        'page': page,
    }
    return render(request, 'myapp/page.html', context)


def post(request):
    post = Post.objects.filter(user__username='apu')

    context = {
        'post': post,
    }
    return render(request, 'myapp/post.html', context)


def song(request):
    song = Song.objects.filter(user__username='moni')

    context = {
        'song': song,
    }
    return render(request, 'myapp/song.html', context)
