from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer
from follows.models import Follow

class FeedPagination(PageNumberPagination):
    page_size = 10  # até 10 posts por página

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        current_user = request.user

        # pega os IDs de quem o usuário está seguindo
        following_ids = (
            Follow.objects
            .filter(follower=current_user)
            .values_list('following_id', flat=True)
        )

        # busca os posts desses usuários, do mais recente ao mais antigo
        feed_posts = (
            Post.objects
            .filter(author_id__in=following_ids)
            .order_by('-created_at')
        )

        # aplica paginação
        paginator = FeedPagination()
        page = paginator.paginate_queryset(feed_posts, request)

        # serializa somente os posts desta página
        serializer = PostSerializer(page, many=True)

        # retorna o resultado paginado com meta de paginação
        return paginator.get_paginated_response(serializer.data)
