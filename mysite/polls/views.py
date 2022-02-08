from multiprocessing import context
import re
from tempfile import template
from unicodedata import name
from django.http import HttpResponseRedirect
from django.shortcuts import render
from polls.models import *
from polls.forms import *
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

def update_person(request, *args, **kwargs):
    template_name = 'update_person.html'
    obj = get_object_or_404(
        Person,
        pk = kwargs.get('pk')
    )
    if request.method == 'GET':
        form = PersonForm(
            initial={
                'name': obj.name,
                'age': obj.age,
            }
        )
        context = {
            'form': form
        }
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form = PersonForm(
            request.POST,
            request.FILES,
            initial={
                'name': obj.name,
                'age': obj.age,
            }
        )
        context = {
            'form': form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.sex = form.cleaned_data.get('sex')
            obj.age = form.cleaned_data.get('age')
            obj.country = form.cleaned_data.get('country')
            obj.save()
            return HttpResponseRedirect("/")
        return render(
            request=request,
            template_name=template_name,
            context=context
        )

def add_person(request):
    template_name = 'add-person.html'

    
    context = {}
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
            
    context['form'] = form
            
    return render(
            request=request,
            template_name=template_name,
            context=context
        )
     

def list_person(request):
    template_name = 'index.html'
    persons = Person.objects.all()
    context ={
        'persons' : persons,
    }
         
    return render(request=request, template_name=template_name, context=context)


def delete_person(request, *args, **kwargs):
    template_name = 'delete.html'
    obj = get_object_or_404(
        Person,
        pk = kwargs.get('pk')
    )
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(
        request=request,
        template_name=template_name
        )


# For Magasin
def list_magasin(request):
    template_name = 'list-magasin.html'
    magasins = Magasin.objects.all()
    context ={
        'magasins' : magasins,
    }
         
    return render(request=request, template_name=template_name, context=context)

def add_magasin(request):
    template_name = 'add-magasin.html'

    
    context = {}
    form = MagasinForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list_magasin")

    context['form'] = form
            
    return render(
            request=request,
            template_name=template_name,
            context=context
        )

def update_magasin(request, *args, **kwargs):
    template_name = 'update-magasin.html'
    obj = get_object_or_404(
        Magasin,
        pk = kwargs.get('pk')
    )
    if request.method == 'GET':
        form = MagasinForm(
            initial={
                'name': obj.name,
                'created_at': obj.created_at,
                'updated_at': obj.updated_at,
            }
        )
        context = {
            'form': form
        }
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form = MagasinForm(
            request.POST,
            request.FILES,
            initial={
                'name': obj.name,
                'created_at': obj.created_at,
                'updated_at': obj.updated_at,
            }
        )
        context = {
            'form': form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.created_at = form.cleaned_data.get('created_at')
            obj.updated_at = form.cleaned_data.get('updated_at')
            obj.country = form.cleaned_data.get('country')
            obj.save()
            return HttpResponseRedirect("/list_magasin")
        return render(
            request=request,
            template_name=template_name,
            context=context
        )

def delete_magasin(request, *args, **kwargs):
    template_name = 'delete.html'
    obj = get_object_or_404(
        Magasin,
        pk = kwargs.get('pk')
    )
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/list_magasin")
    return render(
        request=request,
        template_name=template_name
        )
#for Profil Magasin

def list_profil(request):
    template_name = 'list-profil.html'
    profils = ProfilMagasin.objects.all()
    context ={
        'profils' : profils,
    }
         
    return render(request=request, template_name=template_name, context=context)

def add_profil(request, **kwargs):
    template_name = 'add-profil.html'

    obj = get_object_or_404(
        Magasin,
        pk = kwargs.get('pk')
    )
    objet = ProfilMagasin()
    magasin = Magasin.objects.filter(id=obj.id)
    
    form = ProfilMagasinForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        objet.email = form.cleaned_data.get('email')
        objet.phone = form.cleaned_data.get('phone')
        objet.created_at = form.cleaned_data.get('created_at')
        objet.updated_at = form.cleaned_data.get('updated_at')
        objet.magasin_id = magasin.values().get()['id']
        objet.save()
        return HttpResponseRedirect("/list_profil")

    context = {
        'magasin': magasin,
        'form': form,
    }
            
    return render(
            request=request,
            template_name=template_name,
            context=context
        )

def update_profil(request, *args, **kwargs):
    template_name = 'update-profil.html'
    obj = get_object_or_404(
        ProfilMagasin,
        pk = kwargs.get('pk')
    )
    if request.method == 'GET':
        form = ProfilMagasinForm(
            initial={
                'email': obj.email,
                'phone': obj.phone,
                'created_at': obj.created_at,
                'updated_at': obj.updated_at,
            }
        )
        context = {
            'form': form
        }
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form = ProfilMagasinForm(
            request.POST,
            request.FILES,
            initial={
                'email': obj.email,
                'phone': obj.phone,
                'created_at': obj.created_at,
                'updated_at': obj.updated_at,
            }
        )
        context = {
            'form': form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.email = form.cleaned_data.get('email')
            obj.phone = form.cleaned_data.get('phone')
            obj.created_at = form.cleaned_data.get('created_at')
            obj.updated_at = form.cleaned_data.get('updated_at')
            obj.save()
            return HttpResponseRedirect("/list_profil")
        return render(
            request=request,
            template_name=template_name,
            context=context
        )


#For produit

def list_produit(request):
    template_name = 'list-produit.html'
    produits = Produit.objects.all()
    context ={
        'produits' : produits,
    }
         
    return render(request=request, template_name=template_name, context=context)

def add_produit(request, **kwargs):
    template_name = 'add-produit.html'

    objet = Produit()
    
    form = ProduitForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        objet.name = form.cleaned_data.get('name')
        objet.country = form.cleaned_data.get('country')
        objet.created_at = form.cleaned_data.get('created_at')
        objet.price = form.cleaned_data.get('price')
        objet.updated_at = form.cleaned_data.get('updated_at')
        objet.image = form.cleaned_data.get('image')
        objet.magasin_id = form.cleaned_data.get('magasin_id')
        objet.save()
        return HttpResponseRedirect("/list_produit")

    context = {
        'form': form,
    }
            
    return render(
            request=request,
            template_name=template_name,
            context=context
        )

def update_produit(request, *args, **kwargs):
    template_name = 'update-produit.html'
    obj = get_object_or_404(
        Produit,
        pk = kwargs.get('pk')
    )
    if request.method == 'GET':
        form = ProduitForm(
            initial={
                'name': obj.name,
                'country': obj.country,
                'price':obj.price,
                'created_at': obj.created_at,
                'updated_at': obj.updated_at,
                'image': obj.image,
                'magasin_id': obj.magasin_id,
            }
        )
        context = {
            'form': form
        }
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form = ProduitForm(
            request.POST,
            request.FILES,
            initial={
                'name': obj.name,
                'country': obj.country,
                'price':obj.price,
                'created_at': obj.created_at,
                'updated_at': obj.updated_at,
                'image': obj.image,
                'magasin_id': obj.magasin_id,
            }
        )
        context = {
            'form': form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.country = form.cleaned_data.get('country')
            obj.price = form.cleaned_data.get('price')
            obj.created_at = form.cleaned_data.get('created_at')
            obj.updated_at = form.cleaned_data.get('updated_at')
            obj.image = form.cleaned_data.get('image')
            obj.magasin_id = form.cleaned_data.get('magasin_id')
            obj.save()
            return HttpResponseRedirect("/list_produit")
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
