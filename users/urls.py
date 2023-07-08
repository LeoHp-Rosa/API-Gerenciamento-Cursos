from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import (
    CreateUserView,
    InstructorStudentDetailView,
    StudentListView,
    UserDetailView,
)

urlpatterns = [
    path("users/", CreateUserView.as_view()),
    path("users/profile", UserDetailView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("users/allstud", StudentListView.as_view()),
    path("users/student/<int:pk>", InstructorStudentDetailView.as_view()),
]
