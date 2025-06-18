from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Produit, Facture, LigneFacture
import uuid

# Create your views here.


def accueil(request):
    produits = Produit.objects.all().order_by('-date_peremption')
    return render(request, 'index.html', {'produits': produits})

def detail(request, produit_id):
    produit = Produit.objects.get(id=produit_id)
    return render(request, 'detail.html', {'produit': produit})

def supprimer(request, produit_id):
    produit = Produit.objects.get(id=produit_id)
    produit.delete()
    return redirect('accueil')

def ajouter(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        date_peremption = request.POST.get('date_peremption')
        Produit.objects.create(nom=nom, description=description, prix=prix, date_peremption=date_peremption)
        return redirect('accueil')
    return render(request, 'ajouter.html')

def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        produit.nom = request.POST.get('nom')
        produit.description = request.POST.get('description')
        produit.prix = request.POST.get('prix')
        produit.date_peremption = request.POST.get('date_peremption')
        produit.save()
        return redirect('detail_produit', produit_id)
    return render(request, 'modifier_produit.html', {'produit': produit})

def selection_produits(request):
    if request.method == 'POST':
        # Créer une nouvelle facture
        numero_facture = f"FAC-{uuid.uuid4().hex[:8].upper()}"
        facture = Facture.objects.create(numero=numero_facture)
        
        # Ajouter les produits sélectionnés
        produits_selectionnes = request.POST.getlist('produits')
        quantites = request.POST.getlist('quantites')
        
        for i, produit_id in enumerate(produits_selectionnes):
            if produit_id and quantites[i]:
                produit = Produit.objects.get(id=produit_id)
                quantite = int(quantites[i])
                LigneFacture.objects.create(
                    facture=facture,
                    produit=produit,
                    quantite=quantite,
                    prix_unitaire=produit.prix
                )
        
        facture.calculer_total()
        return redirect('detail_facture', facture.id)
    
    produits = Produit.objects.all()
    return render(request, 'selection_produits.html', {'produits': produits})

def detail_facture(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id)
    return render(request, 'detail_facture.html', {'facture': facture})

def liste_factures(request):
    factures = Facture.objects.all().order_by('-date_creation')
    return render(request, 'liste_factures.html', {'factures': factures})

def supprimer_facture(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id)
    facture.delete()
    return redirect('liste_factures')