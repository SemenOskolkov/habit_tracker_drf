from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from good_habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    email = 'test_email@test.ru'
    password = '12ddfs984dsa'
    first_name = 'test_first_name'
    last_name = 'test_first_name'
    phone_number = '+79991110000'
    telegram_chat_id = '@testchatid'

    def setUp(self) -> None:

        self.user = User.objects.create(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            phone_number=self.phone_number,
            telegram_chat_id=self.telegram_chat_id,
        )
        self.user.set_password(self.password)
        # self.user.is_superuser = True
        self.user.save()

        response = self.client.post(
            '/users/token/',
            {
                "email": self.email,
                "password": self.password
            }
        )

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.habit = Habit.objects.create(
            owner=self.user,
            place='Дом',
            time='10:00:00',
            action='Сделать зарядку',
            good_habit_sign=True,
            periodicity=1,
            execution_time='00:02:00',
            sign_publicity=True,

        )

    def test_public_habit_list(self):
        response = self.client.get('/good_habits/habits/public/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_personal_habit_list(self):
        response = self.client.get('/good_habits/habits/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_habit_create(self):  # Создание привычки
        '''CREATE Исходные данные'''
        self.test_place = 'Квартира'
        self.test_time = '15:00:00'
        self.test_action = 'Съесть апельсин'
        self.test_good_habit_sign = True
        self.test_periodicity = 1
        self.test_execution_time = '00:02:00'
        self.test_sign_publicity = True

        response = self.client.post('/good_habits/habit/create/',
                                    {
                                        'owner': self.user.pk,
                                        'place': self.test_place,
                                        'time': self.test_time,
                                        'action': self.test_action,
                                        'good_habit_sign': self.test_good_habit_sign,
                                        'periodicity': self.test_periodicity,
                                        'execution_time': self.test_execution_time,
                                        'sign_publicity': self.test_sign_publicity,
                                    }
                                    )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_get_habit(self):  # Просмотр привычки
        response = self.client.get(
            reverse('good_habit:habit_retrieve', args=[self.habit.pk])
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        expected_data = {
            'id': self.habit.pk,
            'owner': self.user.pk,
            'place': self.habit.place,
            'time': self.habit.time,
            'action': self.habit.action,
            'good_habit_sign': self.habit.good_habit_sign,
            'associated_habit': None,
            'periodicity': self.habit.periodicity,
            'reward': None,
            'execution_time': self.habit.execution_time,
            'sign_publicity': self.habit.sign_publicity,
            'last_run': None,
        }

        self.assertEqual(
            response.json(),
            expected_data
        )

    def test_habit_update(self):  # Изменение привычки
        '''UPDATE Новые данные'''
        self.test_new_place = 'Квартира'
        self.test_new_time = '10:00:00'
        self.test_new_action = 'Съесть яблоко'
        self.test_new_good_habit_sign = True
        self.test_new_periodicity = 1
        self.test_new_execution_time = '00:02:00'
        self.test_new_sign_publicity = True

        response = self.client.patch(
            reverse('good_habit:habit_update', args=[self.habit.pk]),
            {
                'owner': self.user.pk,
                'place': self.test_new_place,
                'time': self.test_new_time,
                'action': self.test_new_action,
                'good_habit_sign': self.test_new_good_habit_sign,
                'periodicity': self.test_new_periodicity,
                'execution_time': self.test_new_execution_time,
                'sign_publicity': self.test_new_sign_publicity,
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.habit.pk,
                'owner': self.user.pk,
                'place': self.test_new_place,
                'time': self.test_new_time,
                'action': self.test_new_action,
                'good_habit_sign': self.test_new_good_habit_sign,
                'associated_habit': None,
                'periodicity': self.test_new_periodicity,
                'reward': None,
                'execution_time': self.test_new_execution_time,
                'sign_publicity': self.test_new_sign_publicity,
                'last_run': None,
            }
        )

    def test_habit_delete(self):  # Удаление привычки
        response = self.client.delete(
            reverse('good_habit:habit_delete', args=[self.habit.pk]))

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
