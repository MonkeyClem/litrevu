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
        widgets = {
            'title': forms.TextInput(attrs={'class': 'ticket-form-input'}),
            'description': forms.Textarea(attrs={'class': 'ticket-form-textarea'}),
            'image': forms.ClearableFileInput(attrs={'class': 'ticket-form-file'}),
        }
