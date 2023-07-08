from django.urls import path

from .views import CreateClassesView, RetrieveUpdateDestroyClassesView

urlpatterns = [path("classes/", CreateClassesView.as_view()),
               path("classes/<int:pk>", RetrieveUpdateDestroyClassesView.as_view())]
