from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur à suivre", max_length=150)
