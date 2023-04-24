from rest_framework import generics

from good_habits.models import Habit
from good_habits.serializers import HabitSerializer, PublicHabitSerializer


class PublicHabitsListView(generics.ListAPIView):
    serializer_class = PublicHabitSerializer
    queryset = Habit.objects.all()


class HabitsListView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitCreatAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
