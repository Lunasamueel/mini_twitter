from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from django.db.models import Count
from users.serializers import UserWithFollowersSerializer

class UserListAPI(ListAPIView):
    serializer_class = UserWithFollowersSerializer

    def get_queryset(self):
        # Anota cada usuário com o número de quem o segue (related_name='followers')
        return User.objects.annotate(
            followers_count=Count('following')
        ).order_by('-followers_count', 'username')
    
