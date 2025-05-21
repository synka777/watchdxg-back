from rest_framework_simplejwt.views import TokenRefreshView
from views import CustomTokenObtainPairView
from django.urls import path, include

urlpatterns = [
    # path('users/', ),
    # path('actions', ),

    # No auth needed for these views
    path('token/', CustomTokenObtainPairView.as_view()), # Login
    path('token/refresh', TokenRefreshView.as_view()), # Keep alive
]
