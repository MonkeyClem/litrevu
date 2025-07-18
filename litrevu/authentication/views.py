from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth import get_user_model
User = get_user_model()


def login_view(request): 
    if request.method == "POST": 
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(f"Authenticating user: {username}")
        if user is not None:
            print('User authenticated successfully')
            login(request, user)  
            return redirect("feed")  
        else:
            form = LoginForm()
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else : 
        form = LoginForm()
    return render(request, 'login_view.html', {'form' : form})


def signup_view(request): 
    if request.method == 'POST':
            print("POSTED THE FORM")
            form = SignUpForm(request.POST) 
            if form.is_valid(): 
                username = form.cleaned_data['username']
                password= form.cleaned_data['password']
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                messages.success(request, "Inscription réussie ! Bienvenue à bord !")
                return redirect("feed")
            else:
                print('Formulaire invalide')
    else:
        form = SignUpForm()  

    return render(request, "signup_view.html", {'form' : form})


