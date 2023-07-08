from rest_framework import serializers

from .models import Classes


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ["id", "title", "description", "date", "link", "status"]
        extra_kwargs = {"id": {"read_only": True}}
