from rest_framework import serializers
from .models import User, Employer

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["id","name","email","age","password","role"]   # Fields to expose in the API
        required_fields = ["email","role"]
        read_only_fields = ["id"]
        
    def create(self, validated_data):
        password = validated_data.pop("password", None)  # Extract the password from validated_data
        user = super().create(validated_data)  # Create the user instance using the remaining data
        if password:
            user.set_password(password)  # Hash the password
            user.save()  # Save the user instance

        # Automatically create an Employer instance if the role is 'employer'
        if validated_data.get("role") == "employer":
            Employer.objects.create(user=user)

        return user
    

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ["id", "user", "company_name", "position"]
        read_only_fields = ["id"]


# Fields are defined in the model to specify how data is stored in the database.
# Fields are defined in the serializer to control how data is represented,
#  validated, and processed in the API.

# validated_data would look like this after the serializer processes the input:
#     validated_data = {
#     "name": "Shazia",
#     "email": "shazia@example.com",
#     "age": 25,
#     "role": "candidate",
#     "password": "test1234"  # Still in plain text at this point
# }