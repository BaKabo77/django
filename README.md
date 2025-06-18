# 🏪 Gestion des Produits et Factures - Django

Une application web Django moderne pour la gestion de produits et la création de factures avec une interface utilisateur intuitive.

## 📋 Table des matières

- [Fonctionnalités](#-fonctionnalités)
- [Technologies utilisées](#-technologies-utilisées)
- [Installation](#-installation)
- [Structure du projet](#-structure-du-projet)
- [Utilisation](#-utilisation)
- [API et URLs](#-api-et-urls)
- [Modèles de données](#-modèles-de-données)
- [Scripts utiles](#-scripts-utiles)
- [Captures d'écran](#-captures-décran)

## ✨ Fonctionnalités

### 🛍️ Gestion des Produits
- **Ajout de produits** : Interface intuitive pour ajouter de nouveaux produits
- **Modification** : Édition facile des informations produit
- **Suppression** : Gestion sécurisée avec confirmation
- **Affichage détaillé** : Vue complète avec toutes les informations
- **Tri par date de péremption** : Organisation automatique des produits

### 🧾 Gestion des Factures
- **Création de factures** : Sélection multiple de produits avec quantités
- **Numérotation automatique** : Génération de numéros uniques (FAC-XXXXXXXX)
- **Calcul automatique** : Totaux et sous-totaux calculés automatiquement
- **Historique** : Liste complète de toutes les factures créées
- **Suppression** : Gestion des factures avec confirmation

### 🎨 Interface Utilisateur
- **Design responsive** : Compatible mobile et desktop
- **Bootstrap 5** : Interface moderne et professionnelle
- **Navigation intuitive** : Barre de navigation claire
- **Feedback utilisateur** : Messages de confirmation et d'erreur
- **Icônes** : Interface visuelle attrayante

## 🛠️ Technologies utilisées

- **Backend** : Django 4.x
- **Base de données** : SQLite
- **Frontend** : Bootstrap 5, HTML5, CSS3
- **Langage** : Python 3.x
- **Système de templates** : Django Templates

## 📦 Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le projet**
```bash
git clone <url-du-repo>
cd django
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
```

3. **Activer l'environnement virtuel**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Installer les dépendances**
```bash
pip install django
```

5. **Configurer la base de données**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Créer un superutilisateur (optionnel)**
```bash
python manage.py createsuperuser
```

7. **Lancer le serveur**
```bash
python manage.py runserver
```

8. **Accéder à l'application**
```
http://127.0.0.1:8000/
```

## 📁 Structure du projet

```
django/
├── mon_projet/              # Configuration principale Django
│   ├── __init__.py
│   ├── settings.py          # Paramètres du projet
│   ├── urls.py              # URLs principales
│   └── wsgi.py
├── app_exo/                 # Application principale
│   ├── __init__.py
│   ├── admin.py             # Interface d'administration
│   ├── models.py            # Modèles de données
│   ├── views.py             # Logique métier
│   ├── urls.py              # URLs de l'application
│   ├── templates/           # Templates HTML
│   │   ├── base.html        # Template de base
│   │   ├── index.html       # Page d'accueil
│   │   ├── detail.html      # Détails produit
│   │   ├── ajouter.html     # Ajout produit
│   │   ├── modifier_produit.html
│   │   ├── selection_produits.html
│   │   ├── liste_factures.html
│   │   └── detail_facture.html
│   └── migrations/          # Migrations de base de données
├── manage.py               # Script de gestion Django
├── db.sqlite3              # Base de données SQLite
├── ajouter_produits_simple.py  # Script d'ajout de produits
└── README.md               # Ce fichier
```

## 🚀 Utilisation

### Navigation principale
1. **Accueil** : Consultez tous les produits disponibles
2. **Ajouter Produit** : Créez de nouveaux produits
3. **Créer Facture** : Sélectionnez des produits et créez une facture
4. **Liste Factures** : Consultez l'historique des factures

### Ajout d'un produit
1. Cliquez sur "Ajouter Produit" dans la navigation
2. Remplissez le formulaire :
   - Nom du produit
   - Description
   - Prix (en euros)
   - Date de péremption
3. Cliquez sur "Ajouter"

### Création d'une facture
1. Cliquez sur "Créer Facture"
2. Cochez les produits désirés
3. Saisissez les quantités
4. Cliquez sur "Créer la Facture"
5. Consultez la facture générée

## 🔗 API et URLs

### URLs principales
- `/` - Page d'accueil (liste des produits)
- `/ajouter/` - Formulaire d'ajout de produit
- `/produit/<id>/` - Détails d'un produit
- `/produit/<id>/modifier/` - Modification d'un produit
- `/produit/<id>/supprimer/` - Suppression d'un produit
- `/facture/selection/` - Création de facture
- `/factures/` - Liste des factures
- `/facture/<id>/` - Détails d'une facture
- `/facture/<id>/supprimer/` - Suppression d'une facture

## 📊 Modèles de données

### Produit
```python
class Produit(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField()
```

### Facture
```python
class Facture(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
```

### LigneFacture
```python
class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
```

## 🔧 Scripts utiles

### Ajout de produits en masse
Utilisez le script `ajouter_produits_simple.py` pour ajouter rapidement des produits d'exemple :

```bash
python ajouter_produits_simple.py
```

Ce script ajoute 30 produits variés avec des données réalistes.

### Commandes Django utiles
```bash
# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Accéder au shell Django
python manage.py shell

# Collecter les fichiers statiques
python manage.py collectstatic
```

## 🎨 Captures d'écran

### Page d'accueil
- Liste des produits avec cartes Bootstrap
- Boutons d'action pour chaque produit
- Navigation claire

### Création de facture
- Interface de sélection intuitive
- Gestion des quantités
- Calcul automatique des totaux

### Détails de facture
- Affichage professionnel
- Tableau détaillé des lignes
- Actions disponibles

## 🔒 Sécurité

- **CSRF Protection** : Tous les formulaires sont protégés
- **Validation des données** : Contrôles côté serveur
- **Confirmation de suppression** : Évite les suppressions accidentelles
- **Gestion d'erreurs** : Messages d'erreur informatifs



### Variables d'environnement
```bash
export DJANGO_SETTINGS_MODULE=mon_projet.settings
export SECRET_KEY=votre-clé-secrète
export DATABASE_URL=postgresql://user:pass@host:port/db
```

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request



## 👨‍💻 Auteur

**TRAORE**
- Email: traorekoba036@gmail.com
- GitHub: [BaKabo77](https://github.com/BaKabo77)

## 🙏 Remerciements

- [Django](https://www.djangoproject.com/) - Framework web
- [Bootstrap](https://getbootstrap.com/) - Framework CSS
- [Font Awesome](https://fontawesome.com/) - Icônes

---

⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile ! 