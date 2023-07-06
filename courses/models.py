from django.db import models


class StatusChoice(models.TextChoices):
    NI = "Não iniciado"
    EP = "Em progresso"
    CO = "Concluído"


class Courses(models.Model):
    name = models.CharField(max_length=100)
    progress = models.CharField(
        max_length=12, choices=StatusChoice.choices, default=StatusChoice.NI
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "users.Instructor",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="instructor",
    )
    students = models.ManyToManyField("users.Student", related_name="student")
