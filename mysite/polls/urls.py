from unicodedata import name
from polls.views import *
from django.urls import path

from polls.views import(
    list_person,
    update_person
)

urlpatterns = [
    path('', list_person, name='home'),
    
    path('update/<int:pk>/',
    update_person,
    name='update'
    ),

    path('update_magasin/<int:pk>/',
    update_magasin,
    name='update_magasin'
    ),

    path('add',
    add_person,
    name='add'
    ),
    path('delete/<int:pk>/',
    delete_person,
    name='delete'
    ),
    path('delete_magasin/<int:pk>/',
    delete_magasin,
    name='delete_magasin'
    ),

    path('add_magasin',
    add_magasin,
    name='add_magasin'
    ),

    path('list_magasin',
    list_magasin,
    name='list_magasin'
    ),

    path('add_profil/<int:pk>/', 
    add_profil,
    name='add_profil'),

    path('list_profil',
    list_profil,
    name='list_profil'
    ),
    path('update_profil/<int:pk>/',
    update_profil,
    name='update_profil'
    ),

    path('add_produit', 
    add_produit,
    name='add_produit'),

    path('list_produit',
    list_produit,
    name='list_produit'
    ),
    path('update_produit/<int:pk>/',
    update_produit,
    name='update_produit'
    ),

]
