from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import CreateUserView, UserDetailView

urlpatterns = [
    path("users/", CreateUserView.as_view()),
    path("users/profile", UserDetailView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
