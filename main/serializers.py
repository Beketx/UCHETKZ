from rest_framework import serializers
from . import models


class TaskSerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        task = models.Task.objects.create(
            user=self.context['request'].user,
            **validate_data
        )
        return task

    class Meta:
        model = models.Task
        fields = ('id', 'title', 'description', 'deadline', 'status', 'user')
        read_only_fields = ('id', 'user')