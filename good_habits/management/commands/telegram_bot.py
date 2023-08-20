from django.core.management.base import BaseCommand
from telebot import TeleBot

from config import settings

bot = TeleBot(token=settings.TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	"""Получение telegram_chat_id"""
	bot.reply_to(message, f"Добро пожаловть в 'Тркекр привычек'!\nДля регистрации на сайте введите ваш telegram_chat_id: {message.chat.id}")

class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		"""Запуск Телеграмм бота"""

		bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
		bot.load_next_step_handlers()  # Загрузка обработчиков
		bot.infinity_polling()  # Бесконечный цикл бота