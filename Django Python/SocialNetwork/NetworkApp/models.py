from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    age = models.PositiveIntegerField(blank=True, default=18, null=True)
    country = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    cover_picture = models.ImageField(upload_to='cover_pictures/', blank=True)
    facebook_url = models.CharField(max_length=100, blank=True)
    instagram_url = models.CharField(max_length=100, blank=True)
    google_url = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    work_place = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.owner.username


class Friend(models.Model):
    owner = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name='owner')
    friends = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name='friend')

    def __str__(self):
        return self.owner.username


class Message(models.Model):
    sender = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name='receiver')
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    read = models.BooleanField(default=False)
    image = models.ImageField(upload_to='message_pictures/', blank=True)

    def __str__(self):
        return self.sender.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='post_pictures/', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    image = models.ImageField(upload_to='post_pictures/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    VOTE_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]

    vote = models.CharField(choices=VOTE_CHOICES, max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')



