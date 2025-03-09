from rest_framework import serializers
from .models import User    # Import the User model from the models file

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","name","email","age"]   # Fields to expose in the API
