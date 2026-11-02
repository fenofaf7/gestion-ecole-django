from django.shortcuts import render, get_object_or_404, redirect
from .models import Etudiant
from .forms import EtudiantForm

def liste_etudiants(request):
    etudiants = Etudiant.objects.all().order_by("nom")

    return render(
        request,
        "etudiants/liste.html",
        {"etudiants": etudiants}
    )

def ajouter_etudiant(request):

    if request.method == "POST":
        form = EtudiantForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect("liste_etudiants")


    else:
        form = EtudiantForm()

    return render(
        request,   
        "etudiants/formulaire.html",
        {
            "form" : form,
            "titre": "Ajouter un étudiant"
        }    
    )

def detail_etudiant(request , id):

    etudiant = get_object_or_404(Etudiant, id=id)

    return render(
        request,
        "etudiants/detail.html",
        {
            "etudiant": etudiant
        }
    )

def modifier_etudiant(request, id):
    etudiant = get_object_or_404(
        Etudiant,
        id=id
    )

    if request.method == "POST":
        form = EtudiantForm(
            request.POST,
            request.FILES,
            instance=etudiant
        )

        if form.is_valid():
            form.save()
            return redirect("liste_etudiants")

    else:
        form = EtudiantForm(instance=etudiant)

    return render(
        request,
        "etudiants/formulaire.html",
        {
            "form": form,
            "titre": "Modifier un étudiant"
        }
    )


def supprimer_etudiant(request, id):

    etudiant = get_object_or_404(
        Etudiant,
        id=id
    )

    if request.method == "POST":
        etudiant.delete()

        return redirect("liste_etudiants")

    return render(
        request,
        "etudiants/confirmer_suppression.html",
        {
            "etudiant": etudiant
        }
    )