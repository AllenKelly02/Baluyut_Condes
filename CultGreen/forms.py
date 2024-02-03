# forms.py
from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['plant_name', 'species', 'description', 'image']
