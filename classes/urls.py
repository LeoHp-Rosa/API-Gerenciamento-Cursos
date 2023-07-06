from django.urls import path

from .views import CreateClassesView

urlpatterns = [path("classes/", CreateClassesView.as_view())]
