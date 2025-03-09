from django.urls import path
from .views import get_users

urlpatterns = [
    path('users/', get_users),  # API endpoint: /api/users/ # define the path to the get_users function
]