from rest_framework.serializers import ModelSerializer, CharField

from core.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"