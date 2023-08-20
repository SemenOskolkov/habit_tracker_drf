from config import settings
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

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
    

class GetLinkTGBot(APIView):
    permission_classes = [AllowAny]
    
    def get(self, *args, **kwargs):
        return Response({"url": settings.TELEGRAM_LINK})
    