from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .forms import TicketForm
from .models import Ticket
from reviews.forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_or_edit_ticket(request, ticket_id = None) : 
    if ticket_id : 
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        if ticket.user != request.user : 
            return HttpResponseForbidden("Vous ne pouvez modifier que les tickets dont vous êtes le créateur : ")
        else : 
            ticket = ticket 
            print("Ticket :::::>" , ticket)
    else : 
        ticket = None

    if request.method == "POST" : 
        form = TicketForm(request.POST ,request.FILES, instance=ticket)
        if form.is_valid() : 
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            #TODO : 
            # return('STAY ON THE SAME PAGE OR REDIRECT ?')
    else : 
        form = TicketForm(instance=ticket)

    context = {
        'form' : form,
        'title' : 'Modifier un Billet' if ticket else 'Créer un billet',
        'submit_label': 'Mettre à jour' if ticket else "Créer",
    }
    return render (request, 'tickets/create_ticket.html', context)

@login_required
def create_ticket_and_rewiew(request) : 
    if request.method == "POST" : 
        ticket_form = TicketForm(request.POST, request.FILE)
        review_form = ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid() : 
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()

            return redirect("feed")
    else : 
        ticket_form = TicketForm()
        review_form = ReviewForm()

    context = {
        'ticket_form' : ticket_form, 
        'review_form': review_form,
        'title': 'Créer un billet et une critique'    
        }
    return render(request, 'tickets/create_ticket_and_review.html', context)

        

@login_required
def delete_ticket(request, ticket_id) : 
    if ticket_id : 
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        if ticket.user != request.user : 
            return HttpResponseForbidden("Vous ne pouvez supprimer que les tickets dont vous êtes l'auteur")
        else : 
            ticket = ticket
    else : 
        # TODO:
        return redirect('feed')

    if request.method == "POST" :
        ticket.delete()
        #TODO : Uncomment line below once we have the homepage ready
        # redirect('/home')
        return redirect('feed')

    context = {
        'title' : "Supprimer un billet", 
        'submit_label' : "Supprimer",
        'ticket' : ticket

    }
    return render(request, 'tickets/delete_ticket.html', context)