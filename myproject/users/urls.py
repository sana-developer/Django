from django.urls import path
from .views import user_list_create, user_detail, EmployerListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Get access & refresh tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refresh access token
    path('users/', user_list_create), # For GET (all users) & POST (create user)
    path('users/<int:pk>/', user_detail),   # For GET, PUT, DELETE (specific user)
    path('employers/', EmployerListView.as_view(), name='employer_list'),
    ]