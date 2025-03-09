from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import UserSerializer

# Define an API endpoint that responds to GET requests
@api_view(['GET']) # This ensures only GET requests are allowed
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)