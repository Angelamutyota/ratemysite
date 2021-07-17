from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    contact = models.IntegerField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        self.save()

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=155)
    project_image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=255)
    link = models.URLField(max_length=255)
    technologies_used = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return f'{self.title}'

    def save(self):
        self.save()



