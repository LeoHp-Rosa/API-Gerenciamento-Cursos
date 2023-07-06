from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import CreateUserView

urlpatterns = [
    path("users/", CreateUserView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
]
