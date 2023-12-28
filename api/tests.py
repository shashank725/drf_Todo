from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate

from .models import TodoItem, Tag
from api.views import Todo

# Create your tests here.


class TodoItemModelTest(TestCase):
    def setUp(self) -> None:
        self.todo = TodoItem.objects.create(
            title="Test_Task1",
            description="Test Description 1",
            due_date="2023-12-30",
            status="OPEN"
        )
        self.tag = Tag.objects.create(
            value="Python"
        )

    def test_todo_item_creation(self):
        todo_item = TodoItem.objects.get(title="Test_Task1")
        self.assertEqual(todo_item.description, "Test Description 1")

    def test__str__(self):
        self.assertEqual(str(self.todo), str(1))
        self.assertEqual(str(self.tag), "Python")


class TodoItemSerializerTest(TestCase):
    def test_serilaizerValidation(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        data = {
            "title": "Serializer",
            "description": "DemoDemo",
            "due_date": "2023-12-25",
            "status": "OPEN"
        }
        request = RequestFactory().post("todos/create/", data)
        force_authenticate(request, user=self.user)
        response = Todo.as_view()(request)
        self.assertRaisesMessage(
            response.data, "Due Date’ field value cannot be before ‘Timestamp created"     # noqa
        )
