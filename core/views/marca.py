from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Marca
from core.serializers import CategoriaSerializer, MarcaSerializer

...
class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer