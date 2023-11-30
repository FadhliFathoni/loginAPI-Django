from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logout successful'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
