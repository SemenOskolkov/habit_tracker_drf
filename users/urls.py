from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreatAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('user/create/', UserCreatAPIView.as_view(), name='user_create'),
]