from django.db import models
from apps.categories.models import Categorie

class Medicament(models.Model):
    """
    Gestion complète du catalogue de médicaments (Image 4.1).
    """
    nom = models.CharField(max_length=255)
    dci = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="medicaments")
    forme = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    
    prix_achat = models.DecimalField(max_digits=10, decimal_places=2)
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
    
    stock_actuel = models.IntegerField(default=0)
    stock_minimum = models.IntegerField(default=5)
    
    date_expiration = models.DateField()
    ordonnance_requise = models.BooleanField(default=False)
    
    # Horodatage automatique (Image 4.1)
    date_creation = models.DateTimeField(auto_now_add=True)
    # Soft delete (Image 4.1)
    est_actif = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return f"{self.nom} ({self.dosage})"

    @property
    def est_en_alerte(self):
        """Alerte si le stock est inférieur au seuil (Image 4.1)."""
        return self.stock_actuel <= self.stock_minimum