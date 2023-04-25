from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.permissions import OwnProfileEditPermission
from users.serializers import UserSerializer


class UserCreatAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [OwnProfileEditPermission]

