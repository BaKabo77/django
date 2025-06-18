#!/usr/bin/env python
"""
Script simple pour ajouter des produits en masse
Usage: python ajouter_produits_simple.py
"""

import os
import sys
import django
from datetime import date, timedelta
import random

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mon_projet.settings')
django.setup()

from app_exo.models import Produit

def ajouter_produits_exemple():
    
    # Données des produits
    produits = [
        # Fruits
        ("Pommes", "Pommes fraîches et croquantes", 2.50),
        ("Bananes", "Bananes mûres et sucrées", 1.80),
        ("Oranges", "Oranges juteuses", 3.20),
        ("Fraises", "Fraises de saison", 4.50),
        ("Raisins", "Raisins noirs sans pépins", 3.80),
        
        # Légumes
        ("Tomates", "Tomates rouges mûres", 2.20),
        ("Carottes", "Carottes fraîches", 1.50),
        ("Poivrons", "Poivrons colorés", 2.80),
        ("Concombres", "Concombres frais", 1.90),
        ("Oignons", "Oignons jaunes", 1.20),
        
        # Produits laitiers
        ("Lait", "Lait frais 1L", 1.10),
        ("Yaourt", "Yaourt nature 4 pots", 2.80),
        ("Fromage", "Fromage râpé 200g", 3.50),
        ("Beurre", "Beurre doux 250g", 2.30),
        ("Crème", "Crème fraîche 200ml", 1.90),
        
        # Viandes
        ("Poulet", "Poulet fermier 1kg", 8.50),
        ("Bœuf", "Steak de bœuf 300g", 12.00),
        ("Porc", "Côte de porc 500g", 6.80),
        ("Poisson", "Filet de poisson 400g", 9.20),
        ("Jambon", "Jambon blanc 200g", 3.80),
        
        # Céréales
        ("Pain", "Pain complet 500g", 2.10),
        ("Riz", "Riz basmati 1kg", 3.50),
        ("Pâtes", "Spaghetti 500g", 1.80),
        ("Céréales", "Céréales muesli 500g", 4.20),
        ("Farine", "Farine T55 1kg", 1.20),
        
        # Boissons
        ("Eau", "Eau minérale 6x1.5L", 3.60),
        ("Jus", "Jus d'orange 1L", 2.90),
        ("Café", "Café en grains 250g", 6.80),
        ("Thé", "Thé vert 50 sachets", 4.50),
        ("Vin", "Vin rouge 75cl", 8.90),
    ]
    
    reponse = input("Voulez-vous supprimer tous les produits existants ? (o/n): ")
    if reponse.lower() in ['o', 'oui', 'y', 'yes']:
        Produit.objects.all().delete()
        print("✅ Tous les produits existants ont été supprimés.")
    
    # Ajouter les nouveaux produits
    produits_crees = 0
    aujourd_hui = date.today()
    
    for nom, description, prix in produits:
        # Générer une date de péremption aléatoire (entre 7 jours et 1 an)
        jours_aleatoires = random.randint(7, 365)
        date_peremption = aujourd_hui + timedelta(days=jours_aleatoires)
        
        # Créer le produit
        produit = Produit.objects.create(
            nom=nom,
            description=description,
            prix=prix,
            date_peremption=date_peremption
        )
        
        produits_crees += 1
        print(f"✅ {produit.nom} - {produit.prix}€ - Péremption: {produit.date_peremption}")
    
    print(f"\n🎉 {produits_crees} produits ont été ajoutés avec succès!")

if __name__ == "__main__":
    ajouter_produits_exemple() 