# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from dateutil.parser import parse

class Note(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title

class TodoList(models.Model):
    note = models.OneToOneField(
        Note,
        on_delete=models.CASCADE
    )
    deadline = models.DateTimeField(auto_now=False)

    def __str__(self):
        today = datetime.date.today()
        deadline = parse(self.deadline)
        delta = deadline - today
        deadlineMessage = ""
        if delta.days > 0:
            deadlineMessage += "{} days left.".format(delta.days)
        else:
            deadlineMessage += "{} have passed.".format(delta.days)
        message = "{} Deadline at: {}. " + deadlineMessage
        return message.format(self.note.title, self.deadline)

class TodoManager(models.Manager):
    def create_todo(self, **kwargs):
        todo = self.create(**kwargs)
        maxPositionIndex = super().get_queryset().filter(TodoList=todo.TodoList).aggregate(Max('positionIndex'))
        todo.positionIndex = maxPositionIndex
        todo.save()
        return todo
    
    def getordered(self, todoListId):
        return super().get_queryset().filter(TodoList=todoListId).order_by('positionIndex')

class TodoThing(models.Model):
    todoList = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.TextField()
    done = models.BooleanField()
    positionIndex = models.IntegerField(default=0)

    objects = TodoManager()

    def __str__(self):
        return self.text