from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreatAPIView, UserUpdateAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('user/create/', UserCreatAPIView.as_view(), name='user_create'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]