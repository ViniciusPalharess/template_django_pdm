from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Marca
...
class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"