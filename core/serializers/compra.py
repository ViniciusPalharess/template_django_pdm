from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from core.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    """Serializer para o modelo ItensCompra."""
    total = SerializerMethodField()

    class Meta:
        model = ItensCompra
        fields = "__all__"
        depth = 2

    def get_total(self, instance):
        """Calcula o total para um item da compra."""
        return instance.quantidade * instance.acessorio.preco


class CompraSerializer(ModelSerializer):
    """Serializer para o modelo Compra."""
    itens = ItensCompraSerializer(many=True, read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    total = SerializerMethodField()

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")

    def update(self, instance, validated_data):
        """Atualiza uma instância de compra."""
        itens_data = validated_data.pop("itens", [])
        
        # Remove todos os itens existentes
        instance.itens.all().delete()
        
        # Cria novos itens
        for item_data in itens_data:
            ItensCompra.objects.create(compra=instance, **item_data)
        
        # Salva a instância atualizada
        instance.save()
        return instance

    def get_total(self, instance):
        """Calcula o total para uma compra."""
        return sum(item.acessorio.preco * item.quantidade for item in instance.itens.all())


class CriarEditarCompraSerializer(ModelSerializer):
    """Serializer para criar ou editar uma compra."""
    def __init__(self, *args, **kwargs):
        from core.serializers import CriarEditarItensCompraSerializer
        super().__init__(*args, **kwargs)
        self.fields['itens'] = CriarEditarItensCompraSerializer(many=True)     

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    def create(self, validated_data):
        """Cria uma nova compra."""
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        
        for item_data in itens_data:
            item_data["preco_item"] = item_data["Carro"].preco
            ItensCompra.objects.create(compra=compra, **item_data)
        
        compra.save()
        return compra

    @property
    def total(self):
        """Calcula o total da compra."""
        return sum(item.preco_item * item.quantidade for item in self.itens.all())


class CriarEditarItensCompraSerializer(ModelSerializer):
    """Serializer para criar ou editar itens de compra."""
    class Meta:
        model = ItensCompra
        fields = ("Carro", "quantidade")

    def validate(self, data):
        """Valida a quantidade de um item em uma compra."""
        if data["quantidade"] > data["Carro"].quantidade:
            raise serializers.ValidationError(
                {"quantidade": "Quantidade solicitada não disponível em estoque."}
            )
        return data


class ComprasSerializer(ModelSerializer):
    """Serializer para o modelo Compra."""
    itens = ItensCompraSerializer(many=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")
