from rest_framework.viewsets import ModelViewSet
from core.models import Acessorio
from core.serializers import AcessorioSerializer, AcessorioDetailSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return AcessorioDetailSerializer
        return AcessorioSerializer