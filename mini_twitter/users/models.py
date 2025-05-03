from django.contrib.auth.models import User
from rest_framework import serializers

      
class UserWithFollowersSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'followers_count']

