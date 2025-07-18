from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Review
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.http import HttpResponseForbidden
from django.contrib import messages


# Create your views here.

@login_required
def create_review(request, ticket_id ) : 
    ticket = get_object_or_404(Ticket, pk=ticket_id)

    existing_reviews = Review.objects.filter(user = request.user, ticket = ticket).first()
    if existing_reviews : 
        messages.warning(request, "Tu as déjà posté une critique concernant ce ticket")
    if request.method == "POST" : 
        form =  ReviewForm(request.POST)
        if form.is_valid() : 
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('feed')

    else : 
        form = ReviewForm()

    return render(request, "reviews/create_review.html", {'form' : form, 'ticket' : ticket,'title' : 'Publier une critique', 'submit_label' : 'Publier'})


def edit_review(request, review_id) : 
    review = get_object_or_404(Review, pk=review_id)

    if review.user != request.user : 
        return HttpResponseForbidden('Seul le créateur de la critique est autorisé à la modifier')
    
    if request.method == "POST" : 
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid() : 
            form.save()
            return redirect("feed")

    else : 
        form = ReviewForm(instance=review)

    return render(request, "reviews/edit_review.html" , { 'form' : form, 'ticket': review.ticket, 'title' : 'Modifier votre critique', 'submit_label' : 'Modifier' })

@login_required

def delete_review(request, review_id) : 
    review = get_object_or_404(Review, pk = review_id)

    if review.user != request.user : 
        return HttpResponseForbidden("Seul le créateur d'une critique est autorisé à la supprimer")
        
    if request.method == "POST" : 
        review.delete()
        return redirect("feed")
    return render(request, 'reviews/delete_review.html' , {'review' : review, "ticket": review.ticket})
