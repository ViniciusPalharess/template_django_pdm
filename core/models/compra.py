from django.db import models
from core.models import Compra, Acessorio, User

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    class TipoPagamento(models.IntegerChoices):
        CARTAO_CREDITO = 1, "Cartão de Crédito"
        CARTAO_DEBITO = 2, "Cartão de Débito"
        PIX = 3, "PIX"
        BOLETO = 4, "Boleto"
        TRANSFERENCIA_BANCARIA = 5, "Transferência Bancária"
        DINHEIRO = 6, "Dinheiro"
        OUTRO = 7, "Outro"

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)
    tipo_pagamento = models.IntegerField(choices=TipoPagamento.choices, default=TipoPagamento.CARTAO_CREDITO)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "data", "itens", "tipo_pagamento")

class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    acessorio = models.ForeignKey(Acessorio, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)
    preco_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
