# users/tests/test_auth.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTests(APITestCase):

    def test_register_user(self):
        data = {
            "username": "novo_user",
            "email": "novo@email.com",
            "password": "senha123"
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_jwt_login(self):
        User.objects.create_user(username="teste", email="teste@email.com", password="senha123")
        response = self.client.post('/api/token/', {'username': 'teste', 'password': 'senha123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
