from rest_framework.viewsets import ModelViewSet

from core.models import Marca
from core.serializers import MarcaSerializer, MarcaDetailSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return MarcaDetailSerializer
        return MarcaSerializer