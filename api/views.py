from rest_framework_simplejwt.views import TokenObtainPairView
from serializers import CustomObtainPairSerializer
from django.shortcuts import render
from models import XUser


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer # Just check it the handle/password couple is legit