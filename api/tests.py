from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import force_authenticate

from .models import TodoItem
from api.views import *

# Create your tests here.


class TodoItemModelTest(TestCase):
    def setUp(self) -> None:
        self.todo = TodoItem.objects.create(title="Test_Task1", 
                                description="Test Description 1",)
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
        self.assertEqual(str(self.todo), str(1))


class TodoItemSerializerTest(TestCase):

    def test_serilaizerValidation(self):
        self.user = User.objects.create_user(username='testuser', 
                                             password='testpassword')
        data = {"title": "Serializer", 
                "description": "DemoDemo", 
                "due_date": "2023-12-04"}
        request = RequestFactory().post('todos/create/', data)
        force_authenticate(request, user=self.user)
        response = TodoItemCreateView.as_view()(request)
        self.assertRaisesMessage(
            response.data, 
            'Due Date’ field value cannot be before ‘Timestamp created')

