import pandas as pd
from django.core.management.base import BaseCommand
from parfums.models import Parfum

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        df = pd.read_csv("c:/users/chella/documents/python/parfum_reco/parfums/data/fragrantica_filtered_final_cleaned_fixed.csv")

        parfums_to_insert = []
        for index, row in df.iterrows():
            nom = row['Perfume']
            if "-" in nom:
                nom = nom.replace("-", " ").title()
            else:
                nom = row['Perfume']
            df.loc[index, 'Perfume'] = nom
            marque = row['Brand']
            if "-" in marque:
                marque = marque.replace("-", " ").title()
            else:
                marque = row['Brand']
            df.loc[index, 'Brand'] = marque
                
            parfum = Parfum(
                nom=nom,
                marque=marque,
                genre=row['Gender'],
                annee=row['Year'],
                notes_tete=row['Top'],
                notes_coeur=row['Middle'],
                notes_fond=row['Base'],
                accords_principaux=row['mainaccord1'] + ', ' + row['mainaccord2'] + ', ' + row['mainaccord3'] + ', ' + row['mainaccord4'] + ', ' + row['mainaccord5'],
                note_moyenne=row['Rating Value'],
                nombre_votes=row['Rating Count']
            )
            parfums_to_insert.append(parfum)

        Parfum.objects.bulk_create(parfums_to_insert)
        print("importation de parfums reussie")
