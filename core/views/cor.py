from rest_framework.viewsets import ModelViewSet

from core.models import Cor
from core.serializers import CorSerializer, CorDetailSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CorDetailSerializer
        return CorSerializer