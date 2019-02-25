
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import TodoModel


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.order_by('-id')

