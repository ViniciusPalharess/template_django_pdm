from rest_framework.viewsets import ModelViewSet
from core.models import Compra, User
from core.serializers import CompraSerializer, CriarEditarCompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()

    def get_queryset(self):
        usuario = self.request.user
        if usuario.tipo_usuario == User.TipoUsuario.GERENTE:
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
