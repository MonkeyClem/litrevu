from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm, loginForm
from authentication.models import User

# Create your views here.

def login_view(request): 
    if request.method == "POST": 
        print("\nPOSTED THE LOGIN FORM\n")
        print("Form ::::" , request)
        form = loginForm(request.POST) 
        username = request.POST.get("username")
        password = request.POST.get("password")
        passwordConfirmation = request.POST.get("passwordConfirmation")
        print(f"userName : {username}, Password : {password}, PasswordConf : {passwordConfirmation}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # 🔐 Connexion de l'utilisateur
            messages.success(request, "Connexion réussie ! 👋")
            return redirect("follow_user")  
            # return redirect('home')  # 🔁 Redirection vers une page protégée ou la home
        else:
            form = loginForm()
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else : 
        form = loginForm()
    return render(request, 'login_view.html', {'form' : form})


def signup_view(request): 
    if request.method == 'POST':
            print("POSTED THE FORM")
            form = SignUpForm(request.POST) 
            if form.is_valid(): 
                print("\n LE FORMULAIRE EST VALIDE : ")
                username = form.cleaned_data['username']
                password= form.cleaned_data['password']
                print("Username: ", username)
                print("password: ", password)
                user = User.objects.create_user(username=username, password=password)
                # Connexion automatique de l'utilisateur après inscription
                login(request, user)
                # Affichage d'un message de confirmation (optionnel)
                messages.success(request, "Inscription réussie ! Bienvenue 🎉")
                #  Redirection vers la page d'accueil après l'inscription
                return redirect("follow_user")  
            else: 
                print('Formulaire invalide')
    else:
        form = SignUpForm()  

    return render(request, "signup_view.html", {'form' : form})


