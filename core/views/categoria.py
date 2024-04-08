from rest_framework.viewsets import ModelViewSet

from core.models import Categoria
from core.serializers import CategoriaSerializer, CategoriaDetailSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CategoriaDetailSerializer
        return CategoriaSerializer