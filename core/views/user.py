from rest_framework.viewsets import ModelViewSet

from core.models import User
from core.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet

from core.serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
