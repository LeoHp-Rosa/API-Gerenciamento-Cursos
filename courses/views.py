from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from classes.models import Classes
from classes.serializers import ClassesSerializer
from users.models import User
from users.permissions import IsInstructor

from .models import Courses, StatusChoice
from .serializers import CoursesSerializer


class CreateCourseView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsInstructor]

    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()


class RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsInstructor]

    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        students_ids = instance.students.values_list("id", flat=True)
        data = serializer.data
        data["students"] = list(students_ids)

        return Response(data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)


class FilterCourseView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        classes = Classes.objects.filter(course=instance)
        classes_serializer = ClassesSerializer(classes, many=True)

        data = serializer.data
        data["classes"] = classes_serializer.data

        return Response(data)


class AddInstructorToCourseView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsInstructor]

    def update(self, request, *args, **kwargs):
        course_id = request.data.get("course_id")
        instructor_id = request.data.get("instructor")

        try:
            course = Courses.objects.get(id=course_id)
        except Courses.DoesNotExist:
            return Response({"message": "Invalid course ID."}, status=400)

        if course.progress == StatusChoice.EP:
            return Response(
                {
                    "message": "Cannot add an instructor to a course that is already in progress."
                },
                status=400,
            )

        instructor = User.objects.filter(id=instructor_id, is_instructor=True).first()

        if not instructor:
            return Response({"message": "Invalid instructor ID."}, status=400)

        if Courses.objects.filter(
            students=instructor, progress=StatusChoice.EP
        ).exists():
            return Response(
                {
                    "message": "The instructor is already associated with a course in progress."
                },
                status=400,
            )

        course.students.add(instructor)

        return Response(
            {"message": "Instructor successfully added to the course."},
            status=200,
        )


class AddStudentToCourseView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsInstructor]

    def update(self, request, *args, **kwargs):
        course_id = request.data.get("course_id")
        students_ids = request.data.get("students", [])

        try:
            course = Courses.objects.get(id=course_id)
        except Courses.DoesNotExist:
            return Response(
                {"message": "Invalid course ID."},
                status=400,
            )

        students = User.objects.filter(id__in=students_ids, is_instructor=False)

        invalid_students_ids = set(students_ids) - set(
            students.values_list("id", flat=True)
        )

        if invalid_students_ids:
            return Response(
                {
                    "message": f"Invalid student IDs: {', '.join(map(str, invalid_students_ids))}"
                },
                status=400,
            )

        course.students.add(*students)

        return Response(
            {"message": "Students successfully added to the course."}, status=200
        )
