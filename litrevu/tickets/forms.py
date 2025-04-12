# tickets/forms.py
from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description','image']
        labels = {
            'title': "Titre du billet",
            'description': "Description",
            'image': 'Image du billet'
        }
