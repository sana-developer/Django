# here we specify a class that will take this model and convert into JSON compatible data
# when we are working with api, we are sending or recieving JSON data

# here in serializer, we will take this instance of the python object inside the models.py
#  and convert it into JSON data or something that we can actually return and interact with from our API

from rest_framework import serializers
from .models import BlogPost

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost 
        fields = "__all__" # this will take all the fields from the model and convert it into JSON data

        # This will serialize (convert) Blog objects into JSON.
# It also helps in deserializing (converting JSON into a valid Blog object for saving to the DB).