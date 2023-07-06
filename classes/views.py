from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.views import Response

from courses.models import Courses

from .models import Classes
from .serializers import ClassesSerializer


class CreateClassesView(generics.CreateAPIView):
    serializer_class = ClassesSerializer
    queryset = Classes.objects.all()

    def perform_create(self, serializer):
        course_name = self.request.data.get("course")

        if not course_name:
            raise ValidationError("Please provide a value for the 'course' field.")

        try:
            course = Courses.objects.get(Q(name__iexact=course_name))
        except Courses.DoesNotExist:
            raise ValidationError("Please define an existing course.")

        serializer.save(course=course)
