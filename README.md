## Трекер полезных привычек

### Описание проекта

Трекер полезных привычек на основе Django REST Framework с подключением TelegramBotAPI. 

Отправка (уведомление) привычек происходит через Telegram bot.

### Основные системные требования:

* Python 3.11
* Django 4.2
* Django REST framework 3.14
* TelegramBotAPI 4.12
* Docker 4.21
* Зависимости (Python) из файла requirements.txt

### Установка необходимого ПО
#### Создание телеграмм бота
https://core.telegram.org/bots#how-do-i-create-a-bot

#### Установка Docker
https://docs.docker.com/engine/install/

проверка версии Docker
```
docker version
```

### Запуск проекта

1. Загрузите проект из Github в директорию, воспользовавшись командой
```
git clone git@github.com:SemenOskolkov/habit_tracker_drf.git
```

2. Перейдите в директорию проекта **habit_tracker_drf**;
```
cd habit_tracker_drf
```

3. Создайте в корне проекта файл **.env** для работы с переменным окружением
```
touch .env
```

4. Заполните файл **.env**, используя шаблон из файла **.env.sample**

5. Создайте образ docker контейнера
```
docker-compose build
```

6. Запустите docker контейнер в фоновом режиме
```
docker-compose up -d
```

Чтобы остановить работу контейнера, используйте команду
```
docker-compose down
```