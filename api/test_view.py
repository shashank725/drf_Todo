from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate

from api.models import TodoItem
from api.views import TodoItemListview, TodoItemCreateView, TodoItemDetailView



class TodoItemAPITest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', 
                                             password='testpassword')
        self.todo_item = TodoItem.objects.create(title="Test Task", 
                                                 description="Test Description")

    def test_get_todo_item_list(self):
        # url = reverse('todo-list')
        request = self.factory.get("todos/")
        force_authenticate(request, user=self.user)
        response = TodoItemListview.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_todo_item(self):
        url = reverse('todo-create')
        data = {'title': 'New Task', 'description': 'New Description'}
        request = self.factory.post(url, data)
        force_authenticate(request, user=self.user)
        response = TodoItemCreateView.as_view()(request)
        self.assertEqual(response.status_code, 201)

    def test_get_todo_item_detail(self):
        url = reverse('todo-detail', kwargs={'pk': self.todo_item.id})
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = TodoItemDetailView.as_view()(request, pk=self.todo_item.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Test Task")

    def test_update_todo_item(self):
        url = reverse('todo-detail', kwargs={'pk': self.todo_item.id})
        data = {'title': 'Updated Task', 'description': 'Updated Description'}
        request = self.factory.put(url, data, content_type='application/json')
        force_authenticate(request, user=self.user)
        response = TodoItemDetailView.as_view()(request, pk=self.todo_item.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Updated Task")

    def test_delete_todo_item(self):
        url = reverse('todo-detail', kwargs={'pk': self.todo_item.id})
        request = self.factory.delete(url)
        force_authenticate(request, user=self.user)
        response = TodoItemDetailView.as_view()(request, pk=self.todo_item.id)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(TodoItem.objects.filter(id=self.todo_item.id).exists())




# class TodoItemAPITest(TestCase):
#     def setUp(self) -> None:
#         # self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             username="shashank", email="shashank@gmail.com", 
#             password="shashank")
#         self.todo_item = TodoItem.objects.create(title="Test_Task3", 
#                                                  description="DemoDemo", 
#                                                  due_date="2023-12-25", 
#                                                  tags="summer, cold, cold, winter, col", 
#                                                  status="OPEN")
        
#         self.client = Client()
#         return super().setUp()

#     def test_TodoItemListview(self):
#         self.authenticate_client()
#         url = reverse('todo-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 1)
