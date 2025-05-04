from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from posts.models import Post
from follows.models import Follow

User = get_user_model()

class FeedTests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='senha123')
        self.user2 = User.objects.create_user(username='user2', password='senha123')
        self.post = Post.objects.create(author=self.user2, content='Post do user2')
        Follow.objects.create(follower=self.user1, following=self.user2)

        # Gerar token JWT para user1
        refresh = RefreshToken.for_user(self.user1)
        self.access_token = str(refresh.access_token)

        # Autenticar o client com JWT
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

