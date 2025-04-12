from django import forms
from .models import Review

class ReviewForm(forms.ModelForm) : 
    class Meta : 
        model = Review
        fields = [
         'headline', 
         "body",
         'rating',  
        ]
        labels = {
            "headline" : "titre",
            "body": "Contenu",
            "rating" : "Note"
        }
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(6)])  # ✅ de 0 à 5
        }
