from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from posts.models import Post, Like

User = get_user_model()

class PostTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='teste', email='teste@email.com', password='senha123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.post = Post.objects.create(author=self.user, content='Post de teste')

    def test_create_post(self):
        response = self.client.post('/api/posts/', {'content': 'Novo post'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_post(self):
        response = self.client.put(f'/api/posts/{self.post.id}/', {'content': 'Atualizado'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.content, 'Atualizado')

    def test_delete_post(self):
        response = self.client.delete(f'/api/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_like_post(self):
        response = self.client.post(f'/api/posts/{self.post.id}/like/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Like.objects.count(), 1)

    def test_duplicate_like(self):
        self.client.post(f'/api/posts/{self.post.id}/like/')
        response = self.client.post(f'/api/posts/{self.post.id}/like/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
