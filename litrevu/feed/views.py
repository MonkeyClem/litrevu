from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from tickets.models import Ticket
from reviews.models import Review
from users_follow.models import UserFollows
from authentication.models import User
from itertools import chain
from django.contrib import messages

# Create your views here.

"""
Cette fonction est conditionnée opar le fait que l'utilisateur soit connecté (le décorateur @login_required le vérifie)
  
Dans un premier temps, on déclare following_users, qui est un appelle à la classe UserFollows, sur laquelle on applique la méthode
filter afin de retourner l'instance de classe correspondant à l'utilisateur procédant à la requête

On déclare ensuite followed_user, qui est un tableau contenant chaque utilisateur suivi par l'utlisateur connecté.
Ce tableau est obtenu par une compréhension de liste, que itère sur chaque élément de following_users et retourne l'attribut followed_user de chaque instance.

Ensuite, on déclare 
"""

@login_required
def feed(request) :  
    following_users = UserFollows.objects.filter(user = request.user)
    followed_users = [follow.followed_user for follow in following_users]
    
    print("followed_users", followed_users)
    print(f"On est dans le feed.views. Following users ==> {following_users}")

    tickets = Ticket.objects.all().annotate(content_type=Value('TICKET', output_field=CharField()))
    reviews = Review.objects.all().annotate(content_type=Value('REVIEW', output_field=CharField()))

    for ticket in tickets : 
        ticket.user_has_reviewed = Review.objects.filter(ticket= ticket, user=request.user).exists()

    posts = sorted(
        chain(tickets, reviews),
        key= lambda post : post.time_created,
        reverse=True
    )

    for post in posts : 
        print(post)

    return render(request, "feed/feed.html" ,{"posts" : posts})

@login_required
def user_posts(request) : 
    user_tickets = Ticket.objects.all().filter(user = request.user)
    user_review = Review.objects.all().filter(user = request.user)

    if not user_tickets.exists() and not user_review.exists() : 
        messages.warning(request, "Vous n'avez encore rien posté !")

    for ticket in user_tickets : 
        ticket.user_has_reviewed = Review.objects.filter(ticket = ticket, user=request.user).exists()
        ticket.content_type = 'TICKET'
    
    reviews = user_review.annotate(content_type=Value('REVIEW', output_field=CharField()))

    posts = sorted(
        chain(
            user_tickets, 
            reviews
            ),
        key = lambda post : post.time_created,
        reverse=False
        )
    
    return render(request, "feed/feed.html", {'posts': posts})
