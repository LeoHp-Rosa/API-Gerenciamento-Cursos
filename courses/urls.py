from django.urls import path

from .views import CreateCourseView

urlpatterns = [path("course/", CreateCourseView.as_view())]
