from django.db import models
from apps.medicaments.models import Medicament

class Vente(models.Model):
    """
    Enregistre les transactions de vente (Image 4.2).
    """
    STATUT_CHOICES = [
        ('EN_COURS', 'En cours'),
        ('COMPLETEE', 'Complétée'),
        ('ANNULEE', 'Annulée'),
    ]

    # Référence auto-générée : VNT-2024-0001
    reference = models.CharField(max_length=20, unique=True, editable=False)
    date_vente = models.DateTimeField(auto_now_add=True)
    total_ttc = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='COMPLETEE')
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.reference:
            import datetime
            count = Vente.objects.count() + 1
            self.reference = f"VNT-{datetime.date.today().year}-{count:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reference

class LigneVente(models.Model):
    """
    Détail de chaque article dans une vente (Image 4.2).
    """
    vente = models.ForeignKey(Vente, related_name="lignes", on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.PROTECT)
    quantite = models.PositiveIntegerField()
    # Snapshot du prix au moment de la vente (Note métier image 4.2/4.3)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantite} x {self.medicament.nom}"