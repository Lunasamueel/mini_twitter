from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'likes_count', 'created_at']
        read_only_fields = ['id', 'author', 'created_at', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()
