from rest_framework import viewsets
from posts.models import Post, Like
from posts.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.utils.translation import gettext_lazy as _

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    #permission_classes = [IsAuthenticated]

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

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request ,pk=None):
        post = self.get_object()
        user = request.user

        if Like.objects.filter(user=user, post=post).exists():
            return Response(
                {'detail':_('Você já curtiu esse post.')},
                status=status.HTTP_400_BAD_REQUEST)
        
        Like.objects.create(user=user, post=post)
        return Response(
            {'detail':_('Post curtido com sucesso.')}, 
            status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user

        try:
            like = Like.objects.get(user=user, post=post)
            like.delete()
            return Response(
            {'detail':_('Curtida removida com sucesso.')}, 
            status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response(
                {'detail':_('Você não curtiu esse post.')},
                status=status.HTTP_400_BAD_REQUEST)



