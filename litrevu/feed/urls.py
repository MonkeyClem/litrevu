from django.urls import path 
from .views import feed, user_posts

urlpatterns = [
    path('', feed, name="feed"),
    path('posts/', user_posts, name='user_posts')
]