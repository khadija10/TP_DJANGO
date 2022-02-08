from array import array
from dataclasses import field, fields
import email
from email.mime import image
from random import choices
from unicodedata import name
from venv import create
from django import forms
from django.conf import settings
from polls.models import *

magasins: array = []
for magasin in Magasin.objects.all():
    magasinelt = (magasin.id, magasin.name)
    magasins.append(magasinelt)


class PersonForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )
    age = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=1,
        widget=forms.NumberInput(
            attrs={
                'type': 'number'
            }
        )
    )
    sex = forms.ChoiceField(
        required=True,  
        choices=[(x,y) for (x,y) in settings.SEXES],    
        widget=forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )
    country = forms.ChoiceField(
        required=True,  
        choices=[(x,y) for (x,y) in settings.COUNTRIES],    
        widget=forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )
    class Meta: 
        model = Person
        fields = [
            'name',
            'sex',
            'age',
            'country'
        ]
    

class MagasinForm(forms.ModelForm):

    name = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )

    country = forms.ChoiceField(
        required=True,  
        choices=[(x,y) for (x,y) in settings.COUNTRIES],    
        widget=forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )
    created_at = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'date'
            }
        )
    )
    updated_at = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta: 
        model = Magasin
        fields = [
            'name',
            'country',
            #'created_at',
            #'updated_at',
        ]
    

#For ProfilMagasin

class ProfilMagasinForm(forms.ModelForm):

    email = forms.EmailField(
        required=True,
        max_length=200,
        min_length=2,
        widget=forms.EmailInput(
            attrs={
                'type': 'email'
            }
        )
    )

    phone = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )
    
    created_at = forms.DateField(
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'date'
            }
        )
    )
    updated_at = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'date'
            }
        )
    )
    
    class Meta: 
        model = ProfilMagasin
        fields = [
            'email',
            'phone',
        ]

#For Produit
class ProduitForm(forms.ModelForm):

    name = forms.CharField(
        required=True,
        max_length=200,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )

    price = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.NumberInput(
            attrs={
                'type': 'number'
            }
        )
    )
    
    created_at = forms.DateField(
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'date'
            }
        )
    )
    updated_at = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'date'
            }
        )
    )

    country = forms.ChoiceField(
        required=True,  
        choices=[(x,y) for (x,y) in settings.COUNTRIES],    
        widget=forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )
    image = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                'type': 'file'
            }
        )
    )

    magasin_id = forms.ChoiceField(
        required=True,  
        choices=[(x,y) for (x,y) in magasins],    
        widget=forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )
    class Meta: 
        model = Produit
        fields = [
            'name',
            'country',
        ]
  