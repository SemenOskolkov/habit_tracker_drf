from django.urls import path

from good_habits.apps import GoodHabitsConfig
from good_habits.views import *

app_name = GoodHabitsConfig.name


urlpatterns = [
    path('habits/public/', PublicHabitsListView.as_view(), name='public_habits_list'),
    path('habits/', HabitsListView.as_view(), name='habits_list'),
    path('habit/create/', HabitCreatAPIView.as_view(), name='habit_create'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView().as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]
