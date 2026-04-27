from rest_framework import viewsets, filters
from rest_framework.response import Response
from .models import Medicament
from .serializers import MedicamentSerializer

class MedicamentViewSet(viewsets.ModelViewSet):
    """
    Gestion des médicaments avec Soft Delete et Recherche (Image 4.1).
    """
    # On ne récupère que les médicaments actifs par défaut
    queryset = Medicament.objects.filter(est_actif=True)
    serializer_class = MedicamentSerializer
    
    # Configuration de la recherche (Image 4.1 : recherche par nom et DCI)
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', 'dci']

    def perform_destroy(self, instance):
        """
        Surcharge de la suppression pour faire un Soft Delete (Image 4.1).
        """
        instance.est_actif = False
        instance.save()
        # On pourrait aussi ajouter un message ici si besoin