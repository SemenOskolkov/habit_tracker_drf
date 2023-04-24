import datetime

from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from good_habits.models import Habit


class RewardValidator:
    '''Исключить одновременный выбор связанной привычки и указания вознаграждения'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('reward'):
            if value.get('associated_habit'):
                raise ValidationError('Исключен одновременный выбор связанной привычки и указания вознаграждения')


class LeadTimeValidator:
    '''Время выполнения должно быть не больше 120 секунд'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        lead_time = value.get('execution_time')
        max_lead_time = datetime.time(hour=0, minute=2, second=0)
        if lead_time > max_lead_time:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд')


class RewardAndAssociatedHabitNotNullValidator:
    '''Нельзя, чтобы связанная привычка и вознаграждение были одновременно пустые'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        associated_habit = value.get('associated_habit')
        reward = value.get('reward')
        good_habit_sign = value.get('good_habit_sign')
        if not good_habit_sign:
            if (associated_habit is None) and (reward is None):
                raise ValidationError('Нельзя, чтобы связанная привычка и вознаграждение были одновременно пустые')


class AssociatedHabitValidator:
    '''В связанные привычки могут попадать только привычки с признаком приятной привычки'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        associated_habit = value.get('associated_habit')
        if associated_habit:
            object_item = get_object_or_404(Habit, pk=associated_habit.pk)
            if not object_item.good_habit_sign:
                raise ValidationError(
                    'В связанные привычки могут попадать только привычки с признаком приятной привычки')


class GoodHabitValidator:
    '''У приятной привычки не может быть вознаграждения или связанной привычки'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        good_habit_sign = value.get('good_habit_sign')
        associated_habit = value.get('associated_habit')
        reward = value.get('reward')

        if good_habit_sign:
            if associated_habit is not None or reward is not None:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class PeriodicityValidator:
    '''Периодичность не может быть более 7 дней, то есть привычку нельзя выполнять больше, чем раз в неделю'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = value.get('periodicity')

        if periodicity:
            if periodicity > 7:
                raise ValidationError(
                    'Периодичность не может быть более 7 дней, то есть привычку нельзя выполнять больше, чем раз в неделю')
