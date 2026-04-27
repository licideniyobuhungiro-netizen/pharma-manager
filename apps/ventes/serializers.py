from rest_framework import serializers
from django.db import transaction
from .models import Vente, LigneVente
from apps.medicaments.models import Medicament

class LigneVenteSerializer(serializers.ModelSerializer):
    # Pour voir le nom du médicament dans le détail de la vente
    medicament_nom = serializers.ReadOnlyField(source='medicament.nom')

    class Meta:
        model = LigneVente
        fields = ['id', 'medicament', 'medicament_nom', 'quantite', 'prix_unitaire']

class VenteSerializer(serializers.ModelSerializer):
    # Relation imbriquée pour envoyer la vente et ses lignes d'un coup
    lignes = LigneVenteSerializer(many=True)

    class Meta:
        model = Vente
        fields = ['id', 'reference', 'date_vente', 'total_ttc', 'statut', 'notes', 'lignes']
        read_only_fields = ['reference', 'total_ttc', 'date_vente']

    @transaction.atomic
    def create(self, validated_data):
        """
        Logique de création de vente avec déduction de stock (Image 200a5a).
        """
        lignes_data = validated_data.pop('lignes')
        vente = Vente.objects.create(**validated_data)
        total_vente = 0

        for ligne in lignes_data:
            medicament = ligne['medicament']
            quantite = ligne['quantite']

            # 1. Vérification du stock
            if medicament.stock_actuel < quantite:
                raise serializers.ValidationError(
                    f"Stock insuffisant pour {medicament.nom}. Disponible: {medicament.stock_actuel}"
                )

            # 2. Déduction du stock (Exigence Image 200a5a)
            medicament.stock_actuel -= quantite
            medicament.save()

            # 3. Création de la ligne de vente avec snapshot du prix
            LigneVente.objects.create(
                vente=vente,
                medicament=medicament,
                quantite=quantite,
                prix_unitaire=ligne.get('prix_unitaire', medicament.prix_vente)
            )
            
            total_vente += (ligne.get('prix_unitaire', medicament.prix_vente) * quantite)

        # 4. Mise à jour du total final de la vente
        vente.total_ttc = total_vente
        vente.save()
        
        return vente 