from django.urls import path
from .views import follow_user, unfollow_user

urlpatterns = [
    path('follow/', follow_user, name='follow_user'),
    # path('list/', list_following, name='list_following'),
    path('unfollow/<int:follow_id>/', unfollow_user, name='unfollow_user'),
]
