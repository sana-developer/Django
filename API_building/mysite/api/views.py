# this view provide us a way to create  a new blog post and to get all the blog posts that exists

from django.shortcuts import render

# //import generic views that gives us nice view
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.
# using django rest framework

class BlogPostList(generics.ListCreateAPIView):
    # here we're getting all of the different blog posts objects that exits
    queryset = BlogPost.objects.all() 
    # serializer that we want to use when we're actually returning this data, to convert this data into JSON
    serializer_class = BlogPostSerializer

    # now we need to connet it to the url

    # This retrieves all blogs, serializes them, and returns JSON data.
