from rest_framework.viewsets import ModelViewSet
from core.models import Acessorio
from core.serializers import AcessorioSerializer, AcessorioDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["categoria__descricao", "cor__nome"]
    search_fields = ["Marca"]
    filterset_fields = ["usuario", "status", "data"]
    ordering_fields = ["usuario", "status", "data"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return AcessorioDetailSerializer
        return AcessorioSerializer
