from django.http import JsonResponse
from rest_framework import viewsets, mixins, generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .forms import TextAreaChangeForm
from .serializers import UserSerializer
from .utils import create_token, get_token
from rest_framework.authentication import TokenAuthentication
from django.middleware.csrf import get_token

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()

        response = Response()
        response.data = ({
            'message': 'success'
        })
        return response
    
    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateText(request):
    user = request.user
    serializer = UserSerializer(data=request.data, instance=user, partial=True)
    serializer.is_valid()
    serializer.save()
    return Response({"status":"success"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
