from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=100, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=100, verbose_name='Действие')
    good_habit_sign = models.BooleanField(verbose_name='Признак приятной привычки')
    associated_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Связанная привычка')
    periodicity = models.IntegerField(default=1, verbose_name='Периодичность')
    reward = models.CharField(max_length=200, **NULLABLE, verbose_name='Вознаграждение')
    execution_time = models.TimeField(verbose_name='Время на выполнение')
    sign_publicity = models.BooleanField(default=False, verbose_name='Признак публичности')
    last_run = models.DateField(**NULLABLE, verbose_name='Последнее выполнение')

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

    def __str__(self):
        return f'я буду {self.action} в {self.time} в {self.place}'
