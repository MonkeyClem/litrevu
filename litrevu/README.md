# Litrevu 

Une plateforme minimaliste de partage de critiques de livres développée dans le cadre d’un projet OpenClassrooms.

L'utilisateur peut créer des billets (tickets), rédiger des critiques (reviews) pour les billets d'autres utilisateurs, suivre des membres, et consulter un fil d’actualité personnalisé.

---

## Technos

- Python 3.10
- Django 5.x
- HTML / CSS
- SQLite

---

## Fonctionnalités principales

- Inscription et authentification des utilisateurs
- Création de billets de demande de critique
- Rédaction de critiques sur un billet
- Mise à jours des éléments en fonction des permissions 
- Système de suivi d’autres utilisateurs
- Fil d’actualité mixant billets et critiques 
- Possibilité de modifier/supprimer ses propres contenus
- Protection des vues via `@login_required`

---

## 🔧 Installation en local

1. Cloner le projet :
```bash
   git clone https://github.com/MonkeyClem/litrevu.git
>
   cd litrevu
```
 
    Créer un environnement virtuel :

```bash
python3 -m venv env
source env/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Lancer les migrations
```bash
    python manage.py migrate
```

Lancer le serveur :

```bash
python manage.py runserver
```


## Comptes de test (exemple)
FirstTest / password

SecondTest / password123


## Structure des apps
authentication/ : gestion des connexions / inscriptions / logout

tickets/ : création de billets

reviews/ : rédaction de critiques

feed/ : affichage du fil d’actualité

users_follow/ : gestion des abonnements


## Sécurité
Les actions (créer, modifier, supprimer) sont réservées à l’auteur du contenu
CSRF protection activée
Utilisation de l’authentification Django native

## Licence
Projet réalisé dans un cadre pédagogique OpenClassrooms.
Usage personnel uniquement.