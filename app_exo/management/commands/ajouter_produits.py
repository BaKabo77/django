from django.core.management.base import BaseCommand
from django.utils import timezone
from app_exo.models import Produit
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Ajoute des produits d\'exemple à la base de données'

    def add_arguments(self, parser):
        parser.add_argument(
            '--nombre',
            type=int,
            default=20,
            help='Nombre de produits à ajouter (défaut: 20)'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Supprime tous les produits existants avant d\'ajouter'
        )

    def handle(self, *args, **options):
        nombre = options['nombre']
        clear = options['clear']

        if clear:
            Produit.objects.all().delete()
            self.stdout.write(
                self.style.WARNING('Tous les produits existants ont été supprimés.')
            )

        # Données d'exemple pour les produits
        produits_data = [
            # Fruits et légumes
            {"nom": "Pommes Golden", "description": "Pommes sucrées et croquantes, parfaites pour les desserts", "prix": 2.50},
            {"nom": "Bananes Bio", "description": "Bananes biologiques, riches en potassium", "prix": 1.80},
            {"nom": "Tomates Cerises", "description": "Tomates cerises fraîches, idéales pour les salades", "prix": 3.20},
            {"nom": "Carottes", "description": "Carottes fraîches, excellentes pour la santé", "prix": 1.50},
            {"nom": "Salade Laitue", "description": "Laitue fraîche et croquante", "prix": 1.20},
            
            # Produits laitiers
            {"nom": "Lait Entier", "description": "Lait frais entier, 1L", "prix": 1.10},
            {"nom": "Yaourt Nature", "description": "Yaourt nature bio, 4 pots", "prix": 2.80},
            {"nom": "Fromage Comté", "description": "Comté affiné 24 mois, 200g", "prix": 4.50},
            {"nom": "Beurre Doux", "description": "Beurre doux traditionnel, 250g", "prix": 2.30},
            {"nom": "Crème Fraîche", "description": "Crème fraîche épaisse, 200ml", "prix": 1.90},
            
            # Viandes et poissons
            {"nom": "Poulet Fermier", "description": "Poulet fermier élevé en plein air, 1.5kg", "prix": 12.50},
            {"nom": "Saumon Atlantique", "description": "Saumon frais d'Atlantique, 300g", "prix": 8.90},
            {"nom": "Steak Haché", "description": "Steak haché 15% MG, 400g", "prix": 5.20},
            {"nom": "Jambon Blanc", "description": "Jambon blanc de qualité supérieure, 200g", "prix": 3.80},
            {"nom": "Thon Albacore", "description": "Thon albacore en conserve, 160g", "prix": 2.40},
            
            # Céréales et pains
            {"nom": "Pain Complet", "description": "Pain complet aux céréales, 500g", "prix": 2.10},
            {"nom": "Céréales Muesli", "description": "Muesli aux fruits secs, 500g", "prix": 4.20},
            {"nom": "Riz Basmati", "description": "Riz basmati de qualité premium, 1kg", "prix": 3.50},
            {"nom": "Pâtes Spaghetti", "description": "Spaghetti de blé dur, 500g", "prix": 1.80},
            {"nom": "Farine T55", "description": "Farine de blé T55 pour pâtisserie, 1kg", "prix": 1.20},
            
            # Boissons
            {"nom": "Eau Minérale", "description": "Eau minérale naturelle, 6x1.5L", "prix": 3.60},
            {"nom": "Jus d'Orange", "description": "Jus d'orange pressé, 1L", "prix": 2.90},
            {"nom": "Café Arabica", "description": "Café arabica en grains, 250g", "prix": 6.80},
            {"nom": "Thé Vert", "description": "Thé vert bio en sachets, 50 sachets", "prix": 4.50},
            {"nom": "Vin Rouge", "description": "Vin rouge AOC, 75cl", "prix": 8.90},
            
            # Produits d'hygiène
            {"nom": "Dentifrice", "description": "Dentifrice au fluor, 100ml", "prix": 2.30},
            {"nom": "Shampoing", "description": "Shampoing doux, 400ml", "prix": 3.40},
            {"nom": "Savon Liquide", "description": "Savon liquide mains, 500ml", "prix": 2.80},
            {"nom": "Papier Toilette", "description": "Papier toilette 3 épaisseurs, 12 rouleaux", "prix": 4.20},
            {"nom": "Lessive", "description": "Lessive liquide, 2L", "prix": 6.50},
            
            # Produits ménagers
            {"nom": "Liquide Vaisselle", "description": "Liquide vaisselle écologique, 750ml", "prix": 2.10},
            {"nom": "Nettoyant Multi-Usage", "description": "Nettoyant multi-surfaces, 750ml", "prix": 3.20},
            {"nom": "Essuie-Tout", "description": "Essuie-tout 2 épaisseurs, 6 rouleaux", "prix": 2.90},
            {"nom": "Sac Poubelle", "description": "Sacs poubelle 30L, 20 sacs", "prix": 3.80},
            {"nom": "Adoucissant", "description": "Adoucissant parfumé, 1L", "prix": 4.10},
        ]

        # Génération de dates de péremption aléatoires (entre 7 jours et 2 ans)
        aujourd_hui = date.today()
        
        produits_crees = 0
        
        for i in range(min(nombre, len(produits_data))):
            produit_data = produits_data[i]
            
            # Génération d'une date de péremption aléatoire
            jours_aleatoires = random.randint(7, 730)  # Entre 7 jours et 2 ans
            date_peremption = aujourd_hui + timedelta(days=jours_aleatoires)
            
            # Création du produit
            produit = Produit.objects.create(
                nom=produit_data["nom"],
                description=produit_data["description"],
                prix=produit_data["prix"],
                date_peremption=date_peremption
            )
            
            produits_crees += 1
            self.stdout.write(
                f'Produit créé: {produit.nom} - {produit.prix}€ - Péremption: {produit.date_peremption}'
            )

        self.stdout.write(
            self.style.SUCCESS(f'✅ {produits_crees} produits ont été ajoutés avec succès!')
        ) 