from datetime import datetime, timedelta

from celery import shared_task

from good_habits.models import Habit
from good_habits.services import send_message


@shared_task
def time_reminder():
    time = datetime.now()
    habit = Habit.objects.filter(time__hour=time.hour, time__minute=time.minute)

    for habit_item in habit:
        if habit.last_run:
            time_send = habit.last_run + timedelta(days=habit.periodicity)
            if time_send == time.date():
                send_message(habit_item)
                habit_item.last_run = time.date()
                habit_item.save()
        else:
            send_message(habit_item)
            habit_item.last_run = time.date()
            habit_item.save()
