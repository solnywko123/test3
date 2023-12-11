from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.


@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user_data = serializer.validated_data
        CustomUser.objects.create(**user_data)
        return Response({'message': 'User created successfully'}, status=201)
    return Response('Не получилось создать', status=400)


@api_view(['POST'])
def sign_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if password == request.data.get('password'):
        serializer = UserSerializer(user)
        return Response(f'{serializer.data}"Вы успешно вошли" ', status=200)
    else:
        return Response('password is wrong', status=400)





