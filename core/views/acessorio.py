from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Acessorio
from core.serializers import CategoriaSerializer, AcessorioSerializer

...
class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer