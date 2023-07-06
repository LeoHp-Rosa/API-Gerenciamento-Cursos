from django.shortcuts import render
from rest_framework import generics

from .models import Classes
from .serializers import ClassesSerializer


class CreateClassesView(generics.CreateAPIView):
    serializer_class = ClassesSerializer
    queryset = Classes.objects.all()
