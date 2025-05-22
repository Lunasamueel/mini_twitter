from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from posts.models import Post
from posts.serializers import PostSerializer
from follows.models import Follow


class FeedPagination(PageNumberPagination):
    page_size = 10  # até 10 posts por página


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            current_user = request.user

            # IDs dos usuários que o usuário atual está seguindo
            following_ids = Follow.objects.filter(
                follower=current_user
            ).values_list('following_id', flat=True)

            # Posts desses usuários
            feed_posts = Post.objects.filter(
                author_id__in=following_ids
            ).order_by('-created_at')

            # Paginação
            paginator = FeedPagination()
            page = paginator.paginate_queryset(feed_posts, request)

            # Serialização com o contexto do request para verificar likes
            post_serializer = PostSerializer(page, many=True, context={'request': request})

            # Lista de usuários seguidos (para exibir no front se quiser)
            followed_users_list = list(
                current_user.following.values('following__id', 'following__username')
            )

            return paginator.get_paginated_response({
                'posts': post_serializer.data,
                'followed_users': followed_users_list
            })

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
