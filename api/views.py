from rest_framework import generics

from .models import TodoItem
from .serializers import TodoItemSerializer

# Create your views here.


class TodoItemListview(generics.ListAPIView):
    # queryset = TodoItem.objects.all()
    # serializer_class = TodoItemSerializer

    def get_queryset(self):
        return TodoItem.objects.all()

    def get_serializer_class(self):
        return TodoItemSerializer


class TodoItemCreateView(generics.CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class TodoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
