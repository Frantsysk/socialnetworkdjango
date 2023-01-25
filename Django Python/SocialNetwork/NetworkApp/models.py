from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


