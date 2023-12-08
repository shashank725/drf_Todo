from django.urls import path
from api.views import TodoItemListview, TodoItemCreateView, TodoItemDetailView


urlpatterns = [
    path("todos/", TodoItemListview.as_view(), name="todo-list"),
    path("todos/<int:pk>/", TodoItemDetailView.as_view(), name="todo-detail"),
    path("todos/create/", TodoItemCreateView.as_view(), name="todo-create"),
]
