from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import TodoItem
from .serializers import TodoItemSerializer

# Create your views here.


class Todo(APIView):
    def get(self, request, pk=None, format=None):
        if pk is None:
            list = []
            snippets = TodoItem.objects.all()
            for data in snippets:
                tag_list = []
                tags = data.tags.all()
                for i in tags:
                    tag_list.append(i.value)
                data_dict = {
                    'timestamp': data.timestamp,
                    'title': data.title,
                    'description': data.description,
                    'due_date': data.due_date,
                    'tags': tag_list,
                    'status': data.status
                }
                list.append(data_dict)
            return Response(list)
        else:
            snippets = TodoItem.objects.get(id=pk)
            data_dict = res(snippets)
            return Response(data_dict)

    def post(self, request, format=None):
        tag_list = []
        if request.data.get('tags'):
            for i in request.data['tags']:
                tag_list.append({"value": i})
        dict = {
            "title": request.data['title'],
            "description": request.data['description'],
            "due_date": request.data['due_date'],
            "tags": tag_list,
            "status": request.data['status']
        }
        serializer = TodoItemSerializer(data=dict)
        if serializer.is_valid():
            serializer.save()
            model = TodoItem.objects.get(id=serializer.data['id'])
            data = res(model)
            return Response(data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        todo = TodoItem.objects.get(pk=pk)
        tag_list = []
        if request.data.get('tags'):
            for i in request.data['tags']:
                tag_list.append({"value": i})
        dict = {
            "title": request.data['title'],
            "description": request.data['description'],
            "due_date": request.data['due_date'],
            "tags": tag_list,
            "status": request.data['status']
        }
        serializer = TodoItemSerializer(todo, data=dict)
        if serializer.is_valid():
            serializer.save()
            model = TodoItem.objects.get(id=serializer.data['id'])
            data = res(model)
            return Response(data)


def res(snippets):
    tag_list = []
    tags = snippets.tags.all()
    for i in tags:
        tag_list.append(i.value)
    data_dict = {
            'timestamp': snippets.timestamp,
            'title': snippets.title,
            'description': snippets.description,
            'due_date': snippets.due_date,
            'tags': tag_list,
            'status': snippets.status
        }
    return data_dict
