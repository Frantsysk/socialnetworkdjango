from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    age = models.PositiveIntegerField(blank=True, default=18, null=True)
    country = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    facebook_url = models.CharField(max_length=100, blank=True)
    instagram_url = models.CharField(max_length=100, blank=True)
    google_url = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    work_place = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.owner.username



