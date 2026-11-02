from django.db import models

class Cours(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    fichier_pdf = models.FileField(
        upload_to="cours/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titre