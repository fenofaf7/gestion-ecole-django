from django.contrib import admin 
from .models import Etudiant

@admin.register(Etudiant) 
class EtudiantAdmin(admin.ModelAdmin):

    list_display = (

        "nom",

        "prenom",

        "email",

        "age",

        "filiere",
    )

    search_fields = ("nom", "prenom", "email")

    list_filter = ("filiere",)