from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from follows.models import Follow

User = get_user_model()

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        alvo = get_object_or_404(User, pk=pk)

        if alvo == request.user:
            return Response(
                {"detail": "Você não pode seguir a si mesmo."}, status=status.HTTP_400_BAD_REQUEST)
        
        ja_segue = Follow.objects.filter(
            follower=request.user,
            following=alvo
        ).exists()

        if ja_segue:
            return Response(
                {"detail": "Você já está seguindo este usuário."}, status=status.HTTP_400_BAD_REQUEST)

        Follow.objects.create(
            follower=request.user,
            following=alvo
        )
        return Response(
            {"detail": "Agora você segue esse usuário!"},
            status=status.HTTP_201_CREATED
        )

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        alvo = get_object_or_404(User, pk=pk)

        if alvo == request.user:
            return Response(
                {"detail": "Você não pode deixar de seguir a si mesmo."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Tenta buscar o follow existente
        seguimento = Follow.objects.filter(
            follower=request.user,
            following=alvo
        )

        if not seguimento.exists():
            return Response(
                {"detail": "Você não está seguindo este usuário."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Remove o relacionamento de follow
        seguimento.delete()
        return Response(
            {"detail": "Você deixou de seguir este usuário."},
            status=status.HTTP_204_NO_CONTENT
        )

