from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import force_authenticate

from .models import TodoItem
from api.views import TodoItemListview, TodoItemCreateView, TodoItemDetailView

# Create your tests here.


class TodoItemModelTest(TestCase):
    def setUp(self) -> None:
        TodoItem.objects.create(title="Test_Task1", 
                                description="Test Description 1")
        TodoItem.objects.create(title="Test_Task2", 
                                description="Test Description 2", 
                                tags="cold, winter, cold, summer")
        
    def test_todo_item_creation(self):
        todo_item = TodoItem.objects.get(title="Test_Task1")
        self.assertEqual(todo_item.description, "Test Description 1")
    
    def test_tags(self):
        todo_item = TodoItem.objects.get(title="Test_Task2")
        tag = "cold, winter, cold, summer"
        tag = tag.replace(" ", "").split(",")
        tag = set(tag)
        tag = ", ".join(tag)
        self.assertEqual(todo_item.tags, tag)
