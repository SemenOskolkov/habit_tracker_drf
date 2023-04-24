from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    email = 'test_email@test.ru'
    password = '12ddfs984dsa'
    first_name = 'test_first_name'
    last_name = 'test_first_name'
    phone_number = '+79991110000'

    def setUp(self) -> None:

        self.user = User.objects.create(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            phone_number=self.phone_number,
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

        '''CREATE Исходные данные'''
        self.test_email = 'new_test@test.ru'
        self.test_first_name = 'first_name_test'
        self.test_last_name = 'last_name_test'
        self.test_phone_number = '+71234567890'
        self.test_password = 'eofjwn34826w'

    def test_creat_user(self):
        response = self.client.post('/users/user/create/',
                                    {
                                        'email': self.test_email,
                                        'first_name': self.test_first_name,
                                        'last_name': self.test_last_name,
                                        'phone_number': self.test_phone_number,
                                        'password': self.test_password,
                                    }
                                    )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
