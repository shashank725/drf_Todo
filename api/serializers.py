from rest_framework import serializers
from .models import TodoItem

from datetime import datetime


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        # fields = ['title', 'description', 'due_date', 'tags', 'status']
        fields = "__all__"
        read_only_fields = ["timestamp"]

    def validate(self, attrs):
        if attrs.get("due_date"):
            if not attrs.get("timestamp"):
                if attrs.get("due_date") < datetime.now().date():
                    raise serializers.ValidationError(
                        "Due Date’ field value cannot be before ‘Timestamp created"    # noqa
                    )
        return super().validate(attrs)
