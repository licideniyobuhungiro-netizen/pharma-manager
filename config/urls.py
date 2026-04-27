from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Connexion des URLs de tes applications
    path('api/categories/', include('apps.categories.urls')),
    path('api/medicaments/', include('apps.medicaments.urls')),
    path('api/ventes/', include('apps.ventes.urls')),

    # Documentation Swagger (Exigence Smart Holol)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]