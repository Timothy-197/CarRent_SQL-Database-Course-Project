from django import forms

from sys_Purchase.models import  Car, Image

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['description', 'category', 'brand', 'color', 'capacity', 'fuel_type', 'rent_price', 'image']

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ['image']