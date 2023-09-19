from django.db import models
from datetime import datetime

# Create your models here. models is where you define your database
# one for chat room and one for messages
# in django each object has a id when it is created by default


class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    # value is the message the user sends like hey bitch whats up
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)
