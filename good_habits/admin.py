from django.contrib import admin

from good_habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('owner', 'place', 'time', 'action', 'good_habit_sign', 'associated_habit', 'periodicity', 'reward',
                    'execution_time', 'sign_publicity',)
