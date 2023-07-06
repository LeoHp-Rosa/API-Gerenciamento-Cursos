from django.db import models


class Classes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    date = models.DateField()
    link = models.URLField(blank=True)
    status = models.BooleanField(default=False)
