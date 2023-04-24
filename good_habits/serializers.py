from rest_framework import serializers

from good_habits.models import Habit
from good_habits.validators import RewardValidator, LeadTimeValidator, RewardAndAssociatedHabitNotNullValidator, \
    AssociatedHabitValidator, GoodHabitValidator, PeriodicityValidator


class PublicHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        exclude = ['owner']


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardValidator(field=('reward', 'associated_habit')),
            LeadTimeValidator(field='execution_time'),
            RewardAndAssociatedHabitNotNullValidator(field=('associated_habit', 'reward', 'good_habit_sign')),
            AssociatedHabitValidator(field='associated_habit'),
            GoodHabitValidator(field=('good_habit_sign', 'associated_habit', 'reward')),
            PeriodicityValidator(field='periodicity')
        ]
