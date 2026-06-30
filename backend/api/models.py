"""Django models for the task management application."""

from django.db import models


class Task(models.Model):
    """Represents a task with a title, description, and completion status."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
