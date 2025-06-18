from django.db import models

# Create your models here.

class Produit(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField()
    def __str__(self):
        return self.nom

class Facture(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Facture {self.numero}"
    
    def calculer_total(self):
        total = sum(ligne.sous_total for ligne in self.lignes.all())
        self.total = total
        self.save()
        return total

class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='lignes')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def sous_total(self):
        return self.quantite * self.prix_unitaire
