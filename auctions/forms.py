from django import forms
from .models import Listings


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Listings
        fields = ('item_name', 'description', 'category', 'price', 'image', 'owner')
        
