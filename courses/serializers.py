from rest_framework import serializers

from .models import Courses, StatusChoice


class CoursesSerializer(serializers.ModelSerializer):
    progress = serializers.ChoiceField(
        choices=StatusChoice.choices,
        error_messages={
            "invalid_choice": "Opção inválida. As opções válidas são: Não iniciado, Em progresso, Concluído"
        },
    )

    class Meta:
        model = Courses
        fields = ["id", "name", "progress", "start_date", "end_date"]

        extra_kwargs = {"id": {"read_only": True}}
