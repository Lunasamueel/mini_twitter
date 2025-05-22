from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework import status
from follows.models import Follow

User = get_user_model()

class FollowTests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='senha123')
        self.user2 = User.objects.create_user(username='user2', password='senha123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)

    def test_unfollow_user(self):
        # Primeiro, segue o usuário
        self.client.post(f'/api/{self.user2.id}/follow/')
        
        # Depois, deixa de seguir
        response = self.client.post(f'/api/{self.user2.id}/unfollow/')
        
        # Espera-se que o status seja 204 (No Content) quando for bem-sucedido
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verifica se o relacionamento de "follow" foi removido
        self.assertEqual(Follow.objects.filter(follower=self.user1, following=self.user2).count(), 0)
