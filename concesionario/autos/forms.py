from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'description', 'price', 'stock', 'category', 'paisOrigen', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'brand': forms.Select(attrs={'class': 'form-control custom-class'}),
            'description': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'price': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
            'category': forms.Select(attrs={'class': 'form-control custom-class'}),
            'paisOrigen': forms.Select(attrs={'class': 'form-control custom-class'}),
            'image': forms.Select(attrs={'class': 'form-control custom-class'}),
        }


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'description', 'price', 'stock']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'description': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'price': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
        }