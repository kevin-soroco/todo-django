from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Addresses(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    street = models.CharField(max_length=100)
    apartment = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Todo(models.Model):
    todo = models.ForeignKey(Idea, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
