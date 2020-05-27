from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'message': 'User logged in successfully'},
                        status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'User has been registered!',
                'email': user.email,
                'username': user.username,
                'password': user.password,
                'token': token.key,
                'user_id': user.pk
            }, status.HTTP_200_OK)
        else:
            return Response({
                'errors': serializer.errors
            }, status.HTTP_400_BAD_REQUEST)








