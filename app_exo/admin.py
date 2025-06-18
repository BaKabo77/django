from django.contrib import admin
from .models import Produit, Facture, LigneFacture

# Register your models here.
admin.site.register(Produit)
admin.site.register(Facture)
admin.site.register(LigneFacture)
