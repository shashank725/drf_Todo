from rest_framework import serializers
from .models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        # fields = ['title', 'description', 'due_date', 'tags', 'status']
        fields = '__all__'
        read_only_fields = ['account_name']