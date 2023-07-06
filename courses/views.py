from django.shortcuts import render
from rest_framework import generics

from .models import Courses
from .serializers import CoursesSerializer


class CreateCourseView(generics.CreateAPIView):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
