from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin, IsEmployer, IsCandidate
from rest_framework.generics import ListAPIView

from .models import User, Employer
from .serializers import UserSerializer, EmployerSerializer

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated]) # Ensure the user is authenticated
def user_list_create(request):
    if request.method == 'GET':
        # get all users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Create a new user
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save() # Save the new user to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])   # Allow GET, PUT, DELETE for a single user
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT': #Update the user
        serializer = UserSerializer(user, data=request.data, partial=True) # partial=True allows partial updates
        # If you want to update only some fields, set partial=True
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class EmployerListView(ListAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [IsAuthenticated, IsEmployer]




# POST	Create a new resource	Sends data to the server to create something new	Creating a new user (POST /users/)
# PUT	Update an existing resource	Sends data to the server to replace/update an existing resource	Updating an existing user (PUT /users/1/)
