# views.py
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

@authentication_classes([])
@permission_classes([])
class LoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        # Obtém o nome de usuário e senha da requisição
        username = request.data.get('username')
        password = request.data.get('password')

        # Autentica o usuário usando as credenciais fornecidas
        user = authenticate(request, username=username, password=password)

        # Se o usuário for autenticado com sucesso
        if user is not None:
            # Realiza o login do usuário
            login(request, user)

            # Gera ou recupera o token de acesso associado ao usuário
            token, created = Token.objects.get_or_create(user=user)

            # Retorna o token como resposta
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # Se as credenciais estiverem incorretas, retorna uma resposta de erro
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@authentication_classes([])
@permission_classes([])
class LogoutView(views.APIView):
    def post(self, request, *args, **kwargs):
        # Realiza o logout do usuário
        logout(request)

        # Retorna uma resposta indicando que o logout foi bem-sucedido
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
