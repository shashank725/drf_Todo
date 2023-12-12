from rest_framework import serializers
from .models import TodoItem, Tag

from datetime import datetime


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['value']


class TodoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = TodoItem
        fields = ['id', 'timestamp', 'title', 'description',
                  'due_date', 'tags', 'status']
        # fields = "__all__"
        read_only_fields = ["timestamp"]

    def validate(self, attrs):
        if attrs.get("due_date"):
            if not attrs.get("timestamp"):
                if attrs.get("due_date") < datetime.now().date():
                    raise serializers.ValidationError(
                        "Due Date’ field value cannot be before ‘Timestamp created"    # noqa
                    )
        return super().validate(attrs)

    def create(self, validated_data):
        tags_data = self.initial_data.get('tags', [])
        print(tags_data)
        todo_item = TodoItem.objects.create(**validated_data)
        tags = [Tag.objects.get_or_create(value=tag_data['value'])[0]
                for tag_data in tags_data]
        print(tags)
        todo_item.tags.set(tags)
        return todo_item

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.status = validated_data.get('status', instance.status)

        tags_data = self.initial_data.get('tags', [])
        tags = [Tag.objects.get_or_create(value=tag_data['value'])[0]
                for tag_data in tags_data]
        instance.tags.set(tags)

        instance.save()
        return instance
