from django.urls import path
from blog.views import get_index, get_news

urlpatterns = [
    path('', get_index, name='index'),
    path('news', get_news, name='news'),
]