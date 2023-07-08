from django.db import models

from courses.models import Courses


class Classes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    date = models.DateField()
    link = models.URLField(blank=True)
    status = models.BooleanField(default=False)
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE, related_name="classes"
    )
