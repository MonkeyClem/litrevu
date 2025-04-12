from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from tickets.models import Ticket
from reviews.models import Review
from users_follow.models import UserFollows
from authentication.models import User
from itertools import chain
from django.db.models import F

# Create your views here.


@login_required
def feed(request) : 
    # Utilisateurs suivis 
    following_users = UserFollows.objects.filter(user = request.user)
    #Utilisateurs qui nous suivent 
    followed_users = [follow.followed_user for follow in following_users]
    print("followed_users", followed_users)
    print(f"On est dans le feed.views. Following users ==> {following_users}")


    tickets = Ticket.objects.all().annotate(content_type=Value('TICKET', output_field=CharField()))
    reviews = Review.objects.all().annotate(content_type=Value('REVIEW', output_field=CharField()))
    # users = User.objects.all().annotate(content_type=Value('USER', output_field=CharField()), time_created=F("date_joined"))

    posts = sorted(
        chain(tickets, reviews),
        key= lambda post : post.time_created,
        reverse=False
    )

    for post in posts : 
        print(post)

    return render(request, "feed/feed.html" ,{"posts" : posts})