from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Cor
from core.serializers import CategoriaSerializer, CorSerializer

...
class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer