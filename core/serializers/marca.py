from rest_framework import serializers
from core.models import Marca

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class MarcaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"
        depth = 1
