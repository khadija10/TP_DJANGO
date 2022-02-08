from distutils.command import upload
import re
from turtle import mode
from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=20, choices=settings.COUNTRIES)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['name']



class Person(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=20, choices=settings.COUNTRIES)
    age = models.PositiveIntegerField(default=0)
    sex = models.CharField(max_length=10, choices=settings.SEXES)

    def __str__(self) -> str:
        return self.name
    @property
    def isMajor(self):
        return 'Majeur' if self.age>=18 else 'Mineur'
    
    def get_update_url(self):
        return reverse('update', kwargs={'pk':self.id})
    
    def get_delete_url(self):
        return reverse('delete', kwargs={'pk':self.id})

class Magasin(Super):
    def get_update_url(self):
        return reverse('update_magasin', kwargs={'pk':self.id})

    def get_delete_url(self):
        return reverse('delete_magasin', kwargs={'pk':self.id})

class ProfilMagasin(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    magasin = models.OneToOneField(Magasin, on_delete=models.CASCADE, related_name="magasin_profil")

class Produit(Super):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="PRODUCT_IMG")
    magasin = models.ForeignKey(Magasin, on_delete=models.CASCADE, related_name='product_magasin')
