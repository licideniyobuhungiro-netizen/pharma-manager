from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Vente
from .serializers import VenteSerializer

class VenteViewSet(viewsets.ModelViewSet):
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # La logique de déduction de stock est dans le Serializer.create()
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)