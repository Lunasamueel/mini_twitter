# register/views.py
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer

class RegistrationView(CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # aqui usa o create() do serializer

        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'message': 'Usuário registrado com sucesso.'
        }, status=status.HTTP_201_CREATED)
