from rest_framework import serializers
from posts.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    image_url = serializers.SerializerMethodField()
    liked_by_user = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'likes_count', 'created_at', 'image_url', 'liked_by_user']
        read_only_fields = ['id', 'author', 'created_at', 'likes_count', 'image_url']

    def get_liked_by_user(self, post):
        user = self.context['request'].user
        if user.is_authenticated:
            return post.likes.filter(user=user).exists()
        return False

    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_image_url(self, obj):
        return obj.image.url if obj.image else None
