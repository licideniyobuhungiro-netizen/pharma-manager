from rest_framework import serializers
from .models import Medicament

class MedicamentSerializer(serializers.ModelSerializer):
    # Champ calculé pour l'interface (Image 200b53)
    est_en_alerte = serializers.ReadOnlyField()
    # Pour afficher le nom de la catégorie au lieu de l'ID dans les listes
    categorie_nom = serializers.ReadOnlyField(source='categorie.nom')

    class Meta:
        model = Medicament
        fields = [
            'id', 'nom', 'dci', 'categorie', 'categorie_nom', 
            'forme', 'dosage', 'prix_achat', 'prix_vente', 
            'stock_actuel', 'stock_minimum', 'date_expiration', 
            'ordonnance_requise', 'date_creation', 'est_actif', 
            'est_en_alerte'
        ]
        read_only_fields = ['date_creation', 'est_en_alerte']