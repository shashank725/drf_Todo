from django.urls import path
from .views import TodoItemCreateView, TodoItemDetailView, TodoItemListview


urlpatterns = [
    path('todos/', TodoItemListview.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoItemDetailView.as_view(), name='todo-detail'),
    path('todos/create/', TodoItemCreateView.as_view(), name='todo-create'),
]
