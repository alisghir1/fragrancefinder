from django.shortcuts import render
from collections import Counter
from .forms import RecommendedForm
from django.db.models import Q
from .models import Parfum

def recommender(request):
    if request.method == "POST":
        if "reset" in request.POST:
            form = RecommendedForm()
            return render(request, 'parfums/recommender.html', {'form': form})
        form = RecommendedForm(request.POST or None)
        if form.is_valid():
           genre = form.cleaned_data.get('genre')
           selected_perfumes = [
               form.cleaned_data[f"parfum{i}"]
               for i in range(1, 4)
               if form.cleaned_data[f"parfum{i}"] is not None
           ]
        if not selected_perfumes:
           return render(request, 'parfums/recommender.html', {'form' : form, "error" : "Veuillez choisir minimum un parfum"})
        
        all_notes = []
        for perfume in selected_perfumes:
            all_notes.extend(note.strip() for note in perfume.notes_tete.split(','))
            all_notes.extend(note.strip() for note in perfume.notes_coeur.split(','))
            all_notes.extend(note.strip() for note in perfume.notes_fond.split(','))

        note_count = Counter(all_notes)
        notes_frequentes =  [note for note, count in note_count.most_common(7)]

        all_accords = []
        for perfume in selected_perfumes:
            all_accords.extend(perfume.accords_principaux.split(','))
        
        accords_count = Counter(all_accords)
        accords_frequents = [note for note, count in accords_count.most_common(7)]

        parfum_score = {}

        parfums_filtrés = Parfum.objects.exclude(id__in=[p.id for p in selected_perfumes])

        if genre:
            parfums_filtrés = parfums_filtrés.filter(genre=genre)

        for perfume in parfums_filtrés:
            score = 0

            notes_score = 0
            for note in all_notes:
                if note in [n.strip() for n in perfume.notes_tete.split(',')]:
                    notes_score += 1
                    if note in notes_frequentes:
                        notes_score += 2
                elif note in [n.strip() for n in perfume.notes_coeur.split(',')]:
                    notes_score += 1.5
                    if note in notes_frequentes:
                        notes_score += 2
                elif note in [n.strip() for n in perfume.notes_fond.split(',')]:
                    notes_score += 2
                    if note in notes_frequentes:
                        notes_score += 2
            score += notes_score * 1.2

            accord_score = 0
            accords_perfume = perfume.accords_principaux.split(',')
            for i, accord in enumerate(accords_perfume):
                poids = 5 - i
                if accord in all_accords:
                    accord_score += poids
                    if accord in accords_frequents:
                        accord_score += poids * 2
            score += accord_score * 1.4
            
            score = round(score, 1)

            parfum_score[perfume.nom] = score
     
        similar_perfumes = sorted(parfum_score.items(), key=lambda x: x[1], reverse=True)
        top_perfumes_p = [(Parfum.objects.filter(nom=perfume_nom).first(), score) for perfume_nom, score in similar_perfumes[:30]]
        top_perfumes = []
        added_brands = set()


        for perfume, score in top_perfumes_p:
            if perfume.marque not in added_brands:
                top_perfumes.append((perfume, score))
                added_brands.add(perfume.marque)
            if len(top_perfumes) == 10:
                break
        return render(request, 'parfums/recommender.html',
                       {'form' : form,
                        'selected_perfume' : selected_perfumes,
                        'similar_perfumes' : top_perfumes,
                        'notes_frequentes' : notes_frequentes,
                        'accords_frequents' : accords_frequents})
    else:
        form =RecommendedForm()
    return render(request, 'parfums/recommender.html', {'form' : form})