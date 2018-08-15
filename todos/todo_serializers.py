from rest_framework import serializers
from .models import *

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'owner', 'image', 'text')

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'note', 'deadline')

class TodoThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoThing
        fields = ('id', 'todoList', 'text', 'done', 'positionIndex')
