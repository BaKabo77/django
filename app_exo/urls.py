from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('produit/<int:produit_id>/', views.detail, name='detail_produit'),
    path('produit/<int:produit_id>/modifier/', views.modifier_produit, name='modifier_produit'),
    path('produit/<int:produit_id>/supprimer/', views.supprimer, name='supprimer_produit'),
    path('ajouter/', views.ajouter, name='ajouter_produit'),
    path('facture/selection/', views.selection_produits, name='selection_produits'),
    path('facture/<int:facture_id>/', views.detail_facture, name='detail_facture'),
    path('facture/<int:facture_id>/supprimer/', views.supprimer_facture, name='supprimer_facture'),
    path('factures/', views.liste_factures, name='liste_factures'),
] 