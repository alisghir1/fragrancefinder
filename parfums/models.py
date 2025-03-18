from django.db import models
from django.db.models.functions import Lower

class Parfum(models.Model):
    nom = models.CharField(max_length=255)
    marque = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=[('men', 'Homme'), ('women', 'Femme'), ('unisex', 'Unisexe')])
    annee = models.IntegerField(null=True, blank=True)
    notes_tete = models.TextField(null=True, blank=True)
    notes_coeur = models.TextField(null=True, blank=True)
    notes_fond = models.TextField(null=True, blank=True)
    accords_principaux = models.TextField(null=True, blank=True)
    note_moyenne = models.FloatField(null=True, blank=True)
    nombre_votes = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = [Lower('marque'), 'genre', Lower('nom')]

    def __str__(self):
        return f"{self.marque} - {self.nom} - {self.genre}"