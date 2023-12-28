from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate

from api.models import TodoItem, Tag
from api.views import Todo


class TodoItemAPITest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.todo_tag = Tag.objects.create(value='Python')
        self.todo_item = TodoItem.objects.create(
            title="Test Task", description="Test Description",
            due_date="2023-12-30",
            status="OPEN"
        )
        self.todo_item.tags.add(self.todo_tag)

    def test_get_todo_item_list(self):
        request = self.factory.get("todos/")
        force_authenticate(request, user=self.user)
        response = Todo.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_todo_item(self):
        url = reverse("todo-create")
        data = {
            "title": "Buy groceries",
            "description": "Buy groceries from the market",
            "due_date": "2023-12-30",
            "tags": [
                "Food", "Python3"
            ],
            "status": "OPEN"
        }
        request = self.factory.post(url, data)
        force_authenticate(request, user=self.user)
        response = Todo.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_get_todo_item_detail(self):
        url = reverse("todo", kwargs={"pk": self.todo_item.id})
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = Todo.as_view()(request, pk=self.todo_item.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Test Task")

    def test_update_todo_item(self):
        url = reverse("todo-update", kwargs={"pk": self.todo_item.id})
        data = {"title": "Updated Task",
                "description": "Updated Description",
                "due_date": "2023-12-30",
                "tags": ["Food", "Python3"],
                "status": "OPEN"}
        request = self.factory.put(url, data, content_type="application/json")
        force_authenticate(request, user=self.user)
        response = Todo.as_view()(request, pk=self.todo_item.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Updated Task")
