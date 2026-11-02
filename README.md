Installer env : py -m venv .venv
Activer venv : .\.venv\Scripts\Activate.ps1

Installer Django : py -m pip install django

Créer le projet : django-admin startproject config .

créer l'app Etudiant : py manage.py startapp etudiants

dans config/settings on ajoute la table etudiants dans INSTALLED_APPS :
    INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "etudiants",
]

on crée la base : py manage.py migrate

après la création des tables : py -m makemigrations : préparer la migration des tables

puis py manage.py migrate