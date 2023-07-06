from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from courses.serializers import CoursesSerializer

from .models import User
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = UserSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        courses_serializer = CoursesSerializer(user.courses.all(), many=True)
        data = serializer.data
        data["courses"] = courses_serializer.data
        return Response(data)

    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        allowed_fields = ["password", "last_name", "first_name"]
        request_data = {field: request.data.get(field) for field in allowed_fields}

        password = request_data.pop("password", None)
        if password is not None:
            user.set_password(password)

        if not any(request_data.values()):
            return Response(
                {"message": "No allowed fields were provided."}, status=400
            )

        serializer = self.get_serializer(user, data=request_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
