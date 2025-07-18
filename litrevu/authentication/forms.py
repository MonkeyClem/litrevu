from django import forms 
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form) : 
    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    password = forms.CharField(max_length = 63, widget=forms.PasswordInput, label = "Mot de passe")

class SignUpForm(forms.ModelForm) : 
    username = forms.CharField(max_length = 63, label= "Nom d'utilisateur")
    password= forms.CharField(max_length=63, widget=forms.PasswordInput, label="Mot de passe")
    passwordConfirmation= forms.CharField(max_length=63, label="Confirmation Mot de passe")
    
    class Meta : 
        model = User
        fields = ['username', 'password', "passwordConfirmation"]

    def clean_passwordConfirmation(self) : 
        print("\nOn entre dans le clean_passwordConfirmation\n")
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('passwordConfirmation')

        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError("Les mots de passes ne correspondent pas !")
        else: 
            print("Les mots de passe correspondent")

        return password_confirmation