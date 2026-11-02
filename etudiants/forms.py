from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant

        fields = [
            "nom",
            "prenom",
            "email",
            "age",
            "filiere",
            "image",
            "cours",
        ]
        widgets = {
            "cours": forms.CheckboxSelectMultiple()
        }