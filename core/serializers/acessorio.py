from rest_framework import serializers
from core.models import Acessorio

class AcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"

class AcessorioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"
        depth = 1

        ...
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer
...
class Carro(ModelSerializer):
    carro_attachment_key = SlugRelatedField(
        source="carro",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    carro = ImageSerializer(required=False, read_only=True)

...
class CarroSerializer(ModelSerializer):

    carro = ImageSerializer(required=False)
