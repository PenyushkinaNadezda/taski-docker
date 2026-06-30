"""Django REST Framework serializers for the API."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Task model."""

    class Meta:
        """Meta class for TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
