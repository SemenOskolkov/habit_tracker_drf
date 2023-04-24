from rest_framework import serializers

from good_habits.models import Habit


class PublicHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        exclude = ['owner']


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
