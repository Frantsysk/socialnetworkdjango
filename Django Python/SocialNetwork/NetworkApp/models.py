from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='Tell the world your story')
    picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.owner.username



