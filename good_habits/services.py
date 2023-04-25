from config import settings
import requests
from rest_framework.response import Response


def send_message(habit_item):
    text = f'я буду {habit_item.action} в {habit_item.time} в {habit_item.place}'
    data_for_request = {
        "chat_id": habit_item.owner.telegram_chat_id,
        "text": text
    }
    response = requests.get(f'{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage', data_for_request)
    return Response(response.json())
