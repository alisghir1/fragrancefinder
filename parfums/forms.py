from django import forms
from .models import Parfum

class RecommendedForm(forms.Form):
    GENRE_CHOICES = [
        ('', 'Tous'),
        ('men', 'Homme'),
        ('women', 'Femme'),
        ('unisex', 'Unisexe'),
    ]   
    
    parfum1 = forms.ModelChoiceField(queryset=Parfum.objects.all(), required=True, label="Parfum N°1")
    parfum2 = forms.ModelChoiceField(queryset=Parfum.objects.all(), required=False, label="Parfum N°2")
    parfum3 = forms.ModelChoiceField(queryset=Parfum.objects.all(), required=False, label="Parfum N°3")
    parfum4 = forms.ModelChoiceField(queryset=Parfum.objects.all(), required=False,label="Parfum N°4")
    parfum5 = forms.ModelChoiceField(queryset=Parfum.objects.all(), required=False, label="Parfum N°5")
    genre = forms.ChoiceField(choices=GENRE_CHOICES, required=False, label="Genre")