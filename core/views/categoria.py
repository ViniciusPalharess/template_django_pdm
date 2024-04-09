from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models import Categoria
from core.serializers import CategoriaSerializer, CategoriaDetailSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CategoriaDetailSerializer
        return CategoriaSerializer