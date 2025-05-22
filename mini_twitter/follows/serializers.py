from rest_framework import serializers
from follows.models import Follow

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'following', 'follower', 'created_at']
        read_only_fields = ['id', 'created_at', 'follower']
