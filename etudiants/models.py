from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveBigIntegerField()
    filiere = models.CharField(max_length=100)
    date_inscription = models.DateField(auto_now_add=True)

    image = models.ImageField(
        upload_to='etudiant/',
        blank=True,
        null=True
    )

    cours = models.ManyToManyField(
        "cours.Cours",
        related_name="etudiants",
        blank=True
    )

    def __str__(self):
        return f"{self.prenom} {self.nom}"