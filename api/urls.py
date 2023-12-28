from django.urls import path
from api.views import Todo


urlpatterns = [
    path("todos/", Todo.as_view(), name="todo-list"),
    path("todos/<int:pk>/", Todo.as_view(), name="todo"),
    path("todos/create/", Todo.as_view(), name="todo-create"),
    path("todos/create/<int:pk>/", Todo.as_view(), name="todo-update"),
]
