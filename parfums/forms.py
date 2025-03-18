from django import forms
from .models import Parfum

class RecommendedForm(forms.Form):
    GENRE_CHOICES = [
        ('', 'Tous'),
        ('men', 'Homme'),
        ('women', 'Femme'),
        ('unisex', 'Unisexe'),
    ]   
    
    parfum1 = forms.ModelChoiceField(queryset=Parfum.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}), label="")
    parfum2 = forms.ModelChoiceField(queryset=Parfum.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}), label="")
    parfum3 = forms.ModelChoiceField(queryset=Parfum.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}), label="")
    parfum4 = forms.ModelChoiceField(queryset=Parfum.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}), label="")
    parfum5 = forms.ModelChoiceField(queryset=Parfum.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}), label="")
    genre = forms.ChoiceField(choices=GENRE_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-select-sm'}), label="Genre")