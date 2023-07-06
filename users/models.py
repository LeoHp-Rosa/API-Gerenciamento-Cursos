from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=127)
    is_instructor = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_instructor:
            Instructor.objects.create(user=instance)
        else:
            Student.objects.create(user=instance)


models.signals.post_save.connect(create_user_profile, sender=User)
