# Gestion des étudiants — Django

## Présentation du projet

**Gestion des étudiants** est une application web développée avec Django dans le cadre de mon apprentissage du développement web avec Python.

Ce projet a pour objectif de mettre en pratique les concepts fondamentaux de Django à travers la création d'une application simple de gestion des étudiants et de leurs cours.

L'interface utilisateur est réalisée avec **Bootstrap 5** afin de proposer un affichage clair, structuré et responsive.

## Fonctionnalités

L'application permet de :

- **Ajouter un étudiant** : enregistrer les informations d'un nouvel étudiant.
- **Consulter les étudiants** : afficher la liste des étudiants enregistrés.
- **Voir les détails** : consulter les informations détaillées d'un étudiant, notamment sa photo de profil et les cours qu'il suit.
- **Modifier un étudiant** : mettre à jour ses informations personnelles.
- **Supprimer un étudiant** : retirer un étudiant de la base de données après confirmation.
- **Gérer les photos de profil** : importer et afficher une photo pour chaque étudiant.
- **Associer des cours** : relier les étudiants aux cours qu'ils suivent.

## Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Python | Langage de programmation |
| Django | Framework backend |
| HTML5 | Structure des pages |
| CSS3 | Personnalisation des styles |
| Bootstrap 5 | Mise en forme et responsive design |
| SQLite | Base de données |

## Structure du projet

```text
gestion_ecole/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── cours/
│   ├── migrations/
│   ├── models.py
│   ├── admin.py
│   └── views.py
│
├── etudiants/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── etudiants/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

## Installation et configuration

### 1. Cloner le dépôt

```bash
git clone https://github.com/TON-IDENTIFIANT/gestion-ecole-django.git
```

### 2. Accéder au projet

```bash
cd gestion-ecole-django
```

### 3. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 4. Activer l'environnement virtuel

Sous Windows :

```powershell
.venv\Scripts\activate
```

Sous Linux :

```bash
source .venv/bin/activate
```

### 5. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 6. Configurer les variables d'environnement

Créer un fichier `.env` à la racine du projet, puis renseigner :

```env
DJANGO_SECRET_KEY=votre_cle_secrete
```

### 7. Appliquer les migrations

```bash
python manage.py migrate
```

### 8. Lancer le serveur de développement

```bash
python manage.py runserver
```

L'application sera accessible à l'adresse :

http://127.0.0.1:8000/

## Objectif pédagogique

Ce projet constitue une première mise en pratique du framework Django. Il m'a permis de découvrir et d'appliquer plusieurs notions essentielles :

- Architecture d'un projet Django.
- Création de modèles et relations entre les données.
- Utilisation des vues et des URL.
- Création et traitement des formulaires.
- Opérations CRUD.
- Gestion des fichiers et des images.
- Utilisation des templates Django.
- Intégration de Bootstrap 5.

## Auteur

**Feno**

Étudiant en Licence 3 Informatique — Génie Logiciel.

GitHub : https://github.com/fenofaf7