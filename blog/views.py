from django.shortcuts import render
from .models import Post
from django.utils import timezone

def get_index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'index.html', {"posts": posts})

def get_news(request):
    return render(request, 'news.html', {})

def get(request):
    pass

