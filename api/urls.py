from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import XAccountRetrieveView, XUserListView
from django.urls import path


urlpatterns = [
    path('accounts/<str:handle>/', XAccountRetrieveView.as_view()),
    path('users/', XUserListView.as_view()),

    # No auth needed for these views
    path('token/', TokenObtainPairView.as_view()), # Login
    path('token/refresh/', TokenRefreshView.as_view()), # Keep alive
]
