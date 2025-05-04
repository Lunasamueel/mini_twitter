from rest_framework import viewsets
from posts.models import Post, Like
from posts.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from rest_framework.views import APIView


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

    def perform_update(self, serializer):
        post = self.get_object()
        
        if self.request.user != post.author:
            raise PermissionDenied(_("Você não tem permissão para editar esta publicação."))
        serializer.save()
    
    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied(_("Você não tem permissão para apagar esta publicação."))
        instance.delete()


class ToggleLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        user = request.user

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post não encontrado.'}, status=404)

        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        # Retorna também o número atualizado de curtidas
        likes_count = Like.objects.filter(post=post).count()

        return Response({
            'liked': liked,
            'likes_count': likes_count
        }, status=200)

