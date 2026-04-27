from django.contrib import admin
from .models import Medicament

@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
    # Affichage des colonnes selon les champs requis (Image 4.1)
    list_display = ('nom', 'dci', 'categorie', 'stock_actuel', 'stock_minimum', 'prix_vente', 'est_actif')
    list_filter = ('categorie', 'est_actif', 'ordonnance_requise')
    search_fields = ('nom', 'dci')
    # Soft delete visuel (Image 4.1)
    actions = ['desactiver_medicaments']

    def desactiver_medicaments(self, request, queryset):
        queryset.update(est_actif=False)
    desactiver_medicaments.short_description = "Désactiver les médicaments sélectionnés (Soft Delete)"