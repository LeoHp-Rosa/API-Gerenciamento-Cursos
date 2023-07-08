from django.urls import path

from .views import (
    AddInstructorToCourseView,
    AddStudentToCourseView,
    CreateCourseView,
    FilterCourseView,
    RetrieveUpdateDestroyView,
)

urlpatterns = [
    path("courses/", CreateCourseView.as_view()),
    path("courses/<int:pk>", RetrieveUpdateDestroyView.as_view()),
    path("courses/stud/<int:pk>", FilterCourseView.as_view()),
    path("courses/addstud", AddStudentToCourseView.as_view()),
    path("courses/addinst", AddInstructorToCourseView.as_view()),
]
