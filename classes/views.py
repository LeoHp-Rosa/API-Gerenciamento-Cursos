from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from courses.models import Courses
from users.permissions import IsInstructor

from .models import Classes
from .serializers import ClassesSerializer


class CreateClassesView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsInstructor]

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


class RetrieveUpdateDestroyClassesView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsInstructor]
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        try:
            obj = queryset.get(**filter_kwargs)
        except Classes.DoesNotExist:
            raise NotFound("A class with the specified ID does not exist.")
        self.check_object_permissions(self.request, obj)
        return obj
