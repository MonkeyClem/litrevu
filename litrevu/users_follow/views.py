# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserFollows
from .forms import FollowForm
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def follow_user(request) : 
    form = FollowForm()
    following = UserFollows.objects.filter(user = request.user)
    followed_by = UserFollows.objects.filter(followed_user = request.user)
    
    if request.method == "POST" : 
        form = FollowForm(request.POST)
        if form.is_valid() : 
            username_to_follow = form.cleaned_data['username']
            
            if username_to_follow == request.user.username : 
                messages.error(request, "Je comprends, nous aussi on est fan de toi.. Mais tu ne peux pas te suivre toi même")
            else: 
                user_to_follow = get_object_or_404(User, username = username_to_follow)
                follow, created = UserFollows.objects.get_or_create(
                    user = request.user,
                    followed_user = user_to_follow,
                )
                if created : 
                    messages.success(request, f"Tu suis désormais {user_to_follow.username}")
                else : 
                    messages.info(request, f"Tu suis déjà {user_to_follow.username}")

            return redirect('follow_user')
    return render(request, "users_follow/follow_user.html" , {'form' :form, 'following' : following, 'followed_by' : followed_by})


@login_required
def unfollow_user(request, follow_id):
    follow = get_object_or_404(UserFollows, id=follow_id, user=request.user)
    if request.method == 'POST':
        follow.delete()
        messages.success(request, f"Tu as arrêté de suivre {follow.followed_user.username}")
        return redirect('follow_user')
