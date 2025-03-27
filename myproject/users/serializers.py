from rest_framework import serializers
from .models import User    # Import the User model from the models file

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["id","name","email","age","password","role"]   # Fields to expose in the API

    def create(self, validated_data):
        password = validated_data.pop("password", None)  # Extract the password from validated_data
        user = super().create(validated_data)  # Create the user instance using the remaining data
        if password:
            user.set_password(password)  # Hash the password
            user.save()  # Save the user instance
        return user
    
# validated_data would look like this after the serializer processes the input:
#     validated_data = {
#     "name": "Shazia",
#     "email": "shazia@example.com",
#     "age": 25,
#     "role": "candidate",
#     "password": "test1234"  # Still in plain text at this point
# }