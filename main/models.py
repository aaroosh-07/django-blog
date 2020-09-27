from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ToDoList(models.Model):
    author = models.ForeignKey(User , on_delete = models.CASCADE , null = True ,)
    name = models.CharField(max_length = 200)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.ForeignKey(User , on_delete = models.CASCADE , null = True)
    todolist = models.ForeignKey(ToDoList , on_delete = models.CASCADE )
    text = models.CharField(max_length = 300)
    date_posted = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.text

