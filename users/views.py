from django.shortcuts import render
from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
